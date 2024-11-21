import asyncio
import logging
import traceback

import settings
from logger import configure_logging
from main import run
from telegram import send_message

log = logging.getLogger(__name__)


async def start():
    configure_logging(level=settings.LOGGING_LOG_LEVEL)
    try:
        log.info("Starting app")
        await run()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(e)
        if settings.IS_ENABLED_TELEGRAM_LOGGER:
            await send_message(chat_id=int(settings.Envs.TELEGRAM_LOGGER_CHAT_ID), text=traceback.format_exc())
    log.info("Closing app")


if __name__ == "__main__":
    asyncio.run(start())
