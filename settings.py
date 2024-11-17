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
    @dataclass(frozen=True, slots=True)
    class Config:
        # if env variable LOGGING_LOG_LEVEL not set, set default logging level
        default_logging_level: int

    LOCAL = Config(default_logging_level=logging.DEBUG)
    PRODUCTION = Config(default_logging_level=logging.INFO)


class Envs:
    ENVIRONMENT: str = getenv("ENVIRONMENT", Environment.LOCAL)
    LOGGING_LOG_LEVEL: str | None = getenv("LOGGING_LOG_LEVEL", assert_not_none=False)
    COOKIES_HHTOKEN: str = getenv("COOKIES_HHTOKEN")
    COOKIES_HHUID: str = getenv("COOKIES_HHUID")
    COOKIES_XSRF: str = getenv("COOKIES_XSRF")
    TELEGRAM_LOGGER_BOT_TOKEN: str = getenv("TELEGRAM_LOGGER_BOT_TOKEN")
    TELEGRAM_LOGGER_CHAT_ID: str = getenv("TELEGRAM_LOGGER_CHAT_ID")


CURRENT_ENVIRONMENT: Environment.Config = getattr(Environment, Envs.ENVIRONMENT.upper())

if Envs.LOGGING_LOG_LEVEL is None:
    LOGGING_LOG_LEVEL = CURRENT_ENVIRONMENT.default_logging_level
else:
    LOGGING_LOG_LEVEL = int(Envs.LOGGING_LOG_LEVEL)


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
BATCH_UPDATE_URL = "https://rabota.by/shards/resume/batch_update"
