import logging
import os
from dataclasses import dataclass
from typing import TypeVar

try:
    import dotenv
except ImportError:
    pass
else:
    dotenv.load_dotenv("./.env")

T = TypeVar("T")


def getenv(key: str, default: T = None, assert_not_none: bool = True) -> str | T:
    value = os.getenv(key=key, default=default)
    if assert_not_none:
        assert value is not None, f"{key!r} environment variable not set"
    return value


@dataclass(frozen=True, slots=True)
class Environment:
    LOCAL = "local"
    PROD = "production"


ENVIRONMENT_LOGLEVEL_MAP = {
    Environment.LOCAL: logging.DEBUG,
    Environment.PROD: logging.INFO,
}


class Envs:
    ENVIRONMENT: str = getenv("ENVIRONMENT", Environment.LOCAL)
    COOKIES_HHTOKEN: str = getenv("COOKIES_HHTOKEN")
    COOKIES_HHUID: str = getenv("COOKIES_HHUID")
    COOKIES_XSRF: str = getenv("COOKIES_XSRF")
    TELEGRAM_LOGGER_BOT_TOKEN: str = getenv("TELEGRAM_LOGGER_BOT_TOKEN")
    TELEGRAM_LOGGER_CHAT_ID: str = getenv("TELEGRAM_LOGGER_CHAT_ID")


assert Envs.ENVIRONMENT in ENVIRONMENT_LOGLEVEL_MAP, (
    f"Invalid value ({Envs.ENVIRONMENT}) of the environment variable 'ENVIRONMENT'."
    f"Available values: {[*ENVIRONMENT_LOGLEVEL_MAP.keys()]}"
)
LOGGING_LOG_LEVEL = ENVIRONMENT_LOGLEVEL_MAP.get(Envs.ENVIRONMENT)

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
