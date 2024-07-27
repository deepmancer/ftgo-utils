import json
import logging
import orjson
import sys
import pickle
import base64   
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

        logger.opt(depth=depth, exception=record.exc_info, ansi=True).log(
            level, record.getMessage()
        )

def format_record(record: dict) -> str:
    format_string = (
        "<green>{time:HH:mm:ss}</green> | "
        "<level>{level}</level> | "
    )

    if "extra" in record and record["extra"]:
        for binding_key, binding_value in record["extra"].items():
            if binding_key.startswith("custom_bind_"):
                format_string += f"<blue><b>{binding_key[12:].upper()}: {binding_value!r}</b></blue> | "

    format_string += "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    if "payload" in record["extra"]:
        try:
            payload = json.dumps(record["extra"]["payload"], indent=2, default=vars)
            record["extra"]["payload"] = payload
            format_string += "\n<level>Payload: {extra[payload]}</level>\n"
        except pickle.PickleError as e:
            format_string += f"\n<level>Payload could not be serialized: {e}</level>\n"

    if record.get('exception', None) is not None:
        format_string += "{exception}\n"

    return format_string

def init_logging(level: Union[int, str] = logging.INFO):
    import logging
    from loguru import logger

    loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
    )
    for uvicorn_logger in loggers:
        uvicorn_logger.handlers = []

    intercept_handler = InterceptHandler()
    logging.getLogger("uvicorn").handlers = [intercept_handler]
    logging.getLogger("uvicorn.access").handlers = [intercept_handler]
    logging.getLogger("uvicorn.error").handlers = [intercept_handler]
    logging.getLogger("uvicorn.asgi").handlers = [intercept_handler]
    logging.getLogger("uvicorn.error").handlers = [intercept_handler]
    
    # setup the intercept handler as the whole root logger's handler
    logging.root.handlers = [intercept_handler]
    logging.basicConfig(handlers=[InterceptHandler()], level=level, encoding="utf-8", force=True)
    
    logger.configure(
        handlers=[
            {"sink": sys.stdout, "level": level, "colorize": True, "format": format_record},
            {"sink": "logfile.log", "level": level, "format": format_record, "enqueue": True},
        ]
    )

def get_logger(**binding_params):
    from loguru import logger

    if not binding_params:
        return logger
    return logger.bind(**{f"custom_bind_{k}": v for k, v in binding_params.items()})

__all__ = ["init_logging", "get_logger"]
