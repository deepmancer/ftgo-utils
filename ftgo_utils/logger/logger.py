import logging
import sys
from pprint import pformat
from typing import Optional

from loguru import logger
from loguru._defaults import LOGURU_FORMAT

class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )

def format_record(record: dict) -> str:
    format_string = LOGURU_FORMAT
    if record["extra"].get("payload") is not None:
        record["extra"]["payload"] = pformat(
            record["extra"]["payload"], indent=4, compact=True, width=88
        )
        format_string += "\n<level>{extra[payload]}</level>"

    format_string += "{exception}\n"
    return format_string

def init_logging(level=logging.DEBUG, environment: str = "production"):
    import logging
    from loguru import logger

    loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith("uvicorn.")
    )
    for uvicorn_logger in loggers:
        uvicorn_logger.handlers = []

    intercept_handler = InterceptHandler()
    logging.getLogger("uvicorn").handlers = [intercept_handler]

    logger.configure(
        handlers=[
            {"sink": sys.stdout, "level": level, "format": format_record},
            {"sink": "logfile.log", "level": level, "format": format_record, "enqueue": True},
        ]
    )

    logger = logger.bind(env=environment)

def get_logger(layer_name: Optional[str] = None):
    from loguru import logger
    if layer_name is None:
        return logger
    return logger.bind(layer=layer_name)
