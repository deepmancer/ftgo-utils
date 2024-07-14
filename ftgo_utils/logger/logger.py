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
    env = record["extra"].get("env")
    layer = record["extra"].get("layer")

    base_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
        "<magenta>|</magenta> "
        "<level>{level: <8}</level> "
        "<magenta>|</magenta> "
    )

    if env:
        base_format += f"[<yellow>{env.upper()}</yellow>] <magenta>|</magenta> "
    if layer:
        base_format += f"[<yellow>{layer.upper()}</yellow>] <magenta>|</magenta> "

    base_format += (
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> "
        "<magenta>|</magenta> "
        "<level>{message}</level>\n"
    )

    formatted_record = base_format.format_map(record)
    return formatted_record


def init_logging(level=logging.DEBUG):
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
            {"sink": sys.stdout, "level": level, "colorize": True, "format": format_record},
            {"sink": "logfile.log", "level": level, "format": format_record, "enqueue": True},
        ]
    )

def get_logger(layer_name: Optional[str] = None, environment: Optional[str] = None):
    from loguru import logger
    binding_params = {}
    if layer_name is not None:
        binding_params['layer'] = layer_name
    if environment is not None:
        binding_params['env'] = environment

    if not binding_params:
        return logger
    return logger.bind(**binding_params)

    if layer_name is None:
        return logger
    return logger.bind(**binding_params)
