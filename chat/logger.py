import logging
from pathlib import Path

# Create global logger
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers if file is imported multiple times
if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # File logging
    log_dir = Path(__file__).resolve().parent / "logs"
    log_dir.mkdir(exist_ok=True)

    log_file_path = log_dir / "system.log"
    
    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

__all__ = ["logger"]
