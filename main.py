import logging

import requests

import settings

log = logging.getLogger(__name__)


def batch_update() -> requests.Response:
    log.info("Sending batch update request")
    response = requests.post(
        url=settings.BATCH_UPDATE_URL,
        headers={
            "User-Agent": settings.USER_AGENT,
            "Accept": "application/json",
            "X-Xsrftoken": settings.Envs.COOKIES_XSRF,
            "Cookie": f"hhtoken={settings.Envs.COOKIES_HHTOKEN}; hhuid={settings.Envs.COOKIES_HHUID};",
        },
    )
    log.info(
        "Batch update response: %r. Status code: %s",
        response,
        response.status_code,
    )
    log.debug("Batch update response text: %s", response.text)
    return response


def run():
    log.info("Running")
    batch_update()
