import logging
import traceback

import requests

import settings
from logger import configure_logging
from telegram import send_message

log = logging.getLogger(__name__)


def batch_update() -> requests.Response:
    log.info("Sending batch update request")
    response = requests.post(
        url="https://rabota.by/shards/resume/batch_update",
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


if __name__ == "__main__":
    configure_logging(level=settings.LOGGING_LOG_LEVEL)

    try:
        log.info("Starting app")
        run()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(e)
        send_message(chat_id=int(settings.Envs.TELEGRAM_LOGGER_CHAT_ID), text=traceback.format_exc())
    log.info("Closing app")
