import logging
import os
from datetime import datetime

from fastapi import logger

LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

log_filename = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)