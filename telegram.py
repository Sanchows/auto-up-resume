import datetime
import logging

import httpx

import settings

log = logging.getLogger(__name__)


async def send_message(chat_id: int, text: str) -> list[httpx.Response]:
    log.debug("Sending message to chat_id #%s", chat_id)
    text = (
        f"{(datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(hours=3)).strftime("%d.%m.%Y %H:%M:%S")}\n"
        f"{text}"
    )
    url = f"https://api.telegram.org/bot{settings.Envs.TELEGRAM_LOGGER_BOT_TOKEN}/sendMessage"
    responses = []
    while text:
        message = text[:4090]
        text = text[4090:]
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                url=url,
                json={"chat_id": chat_id, "text": message},
                timeout=10,
            )
        responses.append(response)
    log.info("Sent %s messages to chat_id: #%r", len(responses), responses)
    return responses
