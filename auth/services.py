import logging

import settings
from auth.exceptions import AuthStrategyError
from auth.interfaces import AuthStrategy
from auth.strategies import LoginAuth, EnvironmentCookiesAuth

log = logging.getLogger(__name__)


def choose_auth_strategy() -> AuthStrategy:
    log.info("Choosing auth strategy...")
    if all((settings.Envs.COOKIES_HHUID, settings.Envs.COOKIES_XSRF, settings.Envs.COOKIES_HHTOKEN)):
        auth_strategy = EnvironmentCookiesAuth()
    elif all((settings.Envs.USERNAME, settings.Envs.PASSWORD)):
        auth_strategy = LoginAuth()
    else:
        raise AuthStrategyError("It's impossible to choose an auth strategy. Please, check environment variables.")
    log.info("Auth strategy chosen successfully: %r", auth_strategy)
    return auth_strategy
