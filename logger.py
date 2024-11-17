__all__ = ("configure_logging",)

import logging


class Color:
    RESET = "\033[0m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"


LOG_COLORS = {
    logging.DEBUG: Color.BLUE,
    logging.INFO: Color.GREEN,
    logging.WARNING: Color.YELLOW,
    logging.ERROR: Color.RED,
    logging.CRITICAL: Color.MAGENTA,
}


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = LOG_COLORS.get(record.levelno, Color.RESET)
        message = super().format(record)
        return f"{log_color}{message}{Color.RESET}"


LOG_FORMAT = "%(asctime)s.%(msecs)03d %(module)15s:%(lineno)5s %(levelname)8s - %(message)s"
DATEFMT = "%Y-%m-%d %H:%M:%S"


def configure_logging(level: int) -> None:
    handler = logging.StreamHandler()
    formatter = ColoredFormatter(fmt=LOG_FORMAT, datefmt=DATEFMT)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(handler)
