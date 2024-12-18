import logging

import httpx

import settings
from auth.interfaces import AuthStrategy
from auth.services import choose_auth_strategy

log = logging.getLogger(__name__)


async def batch_update(auth_strategy: AuthStrategy) -> httpx.Response:
    hh_session = await auth_strategy.get_hh_session()
    async with httpx.AsyncClient(timeout=10) as client:
        log.debug("Sending batch update request...")
        response = await client.post(
            url=settings.BATCH_UPDATE_URL,
            headers={
                "User-Agent": settings.USER_AGENT,
                "Accept": "application/json",
                "X-Xsrftoken": hh_session.cookies.xsrf,
            },
            cookies={
                "hhtoken": hh_session.cookies.hhtoken,
                "hhuid": hh_session.cookies.hhuid,
            },
        )
    log.info(
        "Batch update response: %r. Status code: %s",
        response,
        response.status_code,
    )

    return response


async def run():
    auth_strategy = choose_auth_strategy()
    await batch_update(auth_strategy=auth_strategy)
