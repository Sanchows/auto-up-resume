from abc import ABC

from hh_session import HHSession


class AuthStrategy(ABC):
    async def get_hh_session(self) -> HHSession:
        pass
