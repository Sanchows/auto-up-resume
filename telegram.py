import datetime
import logging

import httpx

import settings

log = logging.getLogger(__name__)


async def send_message(chat_id: int, text: str) -> list[httpx.Response]:
    log.info("Sending message to chat_id #%s", chat_id)
    text = (
        f"{(datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(hours=3)).strftime("%d.%m.%Y %H:%M:%S")}\n"
        f"{text}"
    )
    url = f"https://api.telegram.org/bot{settings.Envs.TELEGRAM_LOGGER_BOT_TOKEN}/sendMessage"
    responses = []
    while text:
        message = text[:4090]
        text = text[4090:]
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=url,
                json={"chat_id": chat_id, "text": message},
                timeout=10,
            )
        log.info("Sent message to chat #%s. Response: %r", chat_id, response)
        log.debug("Sent message to chat #%s. Response text: %r", chat_id, response.text)
        responses.append(response)
    log.info("Sent %s messages to chat_id: #%", len(responses), responses)
    return responses
