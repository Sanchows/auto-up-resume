import dataclasses


@dataclasses.dataclass(slots=True)
class HHCookies:
    hhuid: str
    xsrf: str
    hhtoken: str | None = None


class HHSession:
    def __init__(self, cookies: HHCookies):
        self.cookies = cookies
