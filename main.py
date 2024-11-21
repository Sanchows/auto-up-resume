import logging

import httpx

import settings

log = logging.getLogger(__name__)


async def batch_update() -> httpx.Response:
    log.info("Sending batch update request")
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=settings.BATCH_UPDATE_URL,
            headers={
                "User-Agent": settings.USER_AGENT,
                "Accept": "application/json",
                "X-Xsrftoken": settings.Envs.COOKIES_XSRF,
            },
            cookies={
                "hhtoken": settings.Envs.COOKIES_HHTOKEN,
                "hhuid": settings.Envs.COOKIES_HHUID,
            },
            timeout=10,
        )
    log.info(
        "Batch update response: %r. Status code: %s",
        response,
        response.status_code,
    )
    log.debug("Batch update response text: %s", response.text)
    log.debug("Batch update response json: %s", response.json())
    return response


async def run():
    log.info("Running")
    await batch_update()
