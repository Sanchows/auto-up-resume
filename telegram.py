import datetime
import json
import logging

import requests

import settings

log = logging.getLogger(__name__)


def send_message(chat_id: int, text: str):
    log.info("Sending message to chat_id #%s", chat_id)
    text = (
        f"{(datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(hours=3)).strftime("%d.%m.%Y %H:%M:%S")}\n"
        f"{text}"
    )
    url = f"https://api.telegram.org/bot{settings.Envs.TELEGRAM_LOGGER_BOT_TOKEN}/sendMessage"
    while text:
        message = text[:4090]
        text = text[4090:]
        response = requests.post(
            url=url,
            data=json.dumps({"chat_id": chat_id, "text": message}),
            headers={"Content-type": "application/json"},
            timeout=10,
        )
        log.info("Sent message to chat #%s. Response: %r", chat_id, response)
        log.debug("Sent message to chat #%s. Response text: %r", chat_id, response.text)
