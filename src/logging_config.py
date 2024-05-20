import logging
import os
from rich.logging import RichHandler


log_level = os.getenv("LOG_LEVEL", "INFO").upper()


logging.basicConfig(
    level=log_level,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)


# Root logger
logger = logging.getLogger("rich")