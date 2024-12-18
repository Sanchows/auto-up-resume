import logging

import httpx

import settings
from auth.interfaces import AuthStrategy
from hh_session import HHSession, HHCookies

log = logging.getLogger(__name__)


class EnvironmentCookiesAuth(AuthStrategy):
    async def get_hh_session(self):
        log.debug("Getting HH session from environment variables...")
        hh_session = HHSession(
            cookies=HHCookies(
                hhuid=settings.Envs.COOKIES_HHUID,
                xsrf=settings.Envs.COOKIES_XSRF,
                hhtoken=settings.Envs.COOKIES_HHTOKEN,
            )
        )
        log.debug("HHSession successfully retrieved: %r", hh_session)
        return hh_session


class LoginAuth(AuthStrategy):
    @staticmethod
    async def _authenticate(username, password) -> HHSession:
        async with httpx.AsyncClient(timeout=10) as client:
            # Делаем обычный GET на главную страницу, чтоб получить hhuid и _xsrf куки
            log.debug(f"Getting 'hhuid', '_xsrf', 'hhtoken' from cookies...")
            response = await client.get(
                url="https://rabota.by/",
                headers={
                    "User-Agent": settings.USER_AGENT,
                },
            )
            hh_session = HHSession(
                cookies=HHCookies(
                    hhuid=response.cookies["hhuid"],
                    xsrf=response.cookies["_xsrf"],
                    hhtoken=response.cookies["hhtoken"],
                )
            )
            log.debug(f"Cookies have been successfully received!")
            log.debug(f"Authenticating by username and password...")
            # Аутентифицируемся, чтоб получить hhtoken куку
            response = await client.post(
                url=settings.LOGIN_URL,
                headers={
                    "User-Agent": settings.USER_AGENT,
                    "Accept": "application/json",
                },
                data={
                    "_xsrf": hh_session.cookies.xsrf,
                    "username": username,
                    "password": password,
                },
                cookies={
                    "_xsrf": hh_session.cookies.xsrf,
                    "hhuid": hh_session.cookies.hhuid,
                    "hhtoken": hh_session.cookies.hhtoken,
                },
            )
        log.info(f"Auth response: %r", response)
        log.info(hh_session.cookies)
        return hh_session

    async def get_hh_session(self):
        log.debug("Getting HH session by authentication...")
        hh_session = await self._authenticate(username=settings.Envs.USERNAME, password=settings.Envs.PASSWORD)
        log.debug("HHSession successfully retrieved: %r", hh_session)
        return hh_session
