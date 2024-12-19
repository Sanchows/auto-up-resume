from abc import ABC, abstractmethod

from hh_session import HHSession


class AuthStrategy(ABC):
    @abstractmethod
    async def get_hh_session(self) -> HHSession:
        pass
