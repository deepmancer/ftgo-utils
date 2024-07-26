import json
import logging
import sys
from typing import Optional, Union

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info, colors=True).log(
            level, record.getMessage()
        )


def format_record(record: dict) -> str:
    from loguru._defaults import LOGURU_FORMAT, env
    format_string = (
        "<green>{time:HH:mm:ss}</green> | "
        "<level>{level}</level> | "
    )
    
    if record["extra"]:
        for binding_key, binding_value in record["extra"].items():
            if binding_key.startswith("custom_bind_"):
                format_string += f"<blue><b>{binding_key[12:].upper()}: {binding_value!r}</b></blue> | "
    
    format_string += "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    if "payload" in record["extra"]:
        payload_str = "payload=dict(" + json.dumps(
            record["extra"]["payload"], indent=4
        )[1:-1] + ")"
        record["extra"]["payload"] = payload_str
        format_string += "\n<level>{extra[payload]}</level>\n"

    if record.get('exc_info') or record.get('exception'):
        format_string += "\n"
        
    format_string += "{exception}\n"
    
    format_obj = env("LOGURU_FORMAT", str, format_string)
    return format_obj

def init_logging(level: Optional[Union[str, int]] = logging.DEBUG):
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
        handlers=[{"sink": sys.stdout, "level": level, "colorize": True, "format": format_record}]
    )

def get_logger(**binding_params):
    if not binding_params:
        return logger
    return logger.bind(**{f"custom_bind_{k}": v for k, v in binding_params.items()})
