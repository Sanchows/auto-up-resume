import logging
import traceback

import settings
from logger import configure_logging
from main import run
from telegram import send_message

log = logging.getLogger(__name__)

configure_logging(level=settings.LOGGING_LOG_LEVEL)

try:
    log.info("Starting app")
    run()
except KeyboardInterrupt:
    pass
except Exception as e:
    log.exception(e)
    if settings.IS_ENABLED_TELEGRAM_LOGGER:
        send_message(chat_id=int(settings.Envs.TELEGRAM_LOGGER_CHAT_ID), text=traceback.format_exc())
log.info("Closing app")
