import logging
import os

def setup_logger(name='plansource_logger'):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # ✅ Prevent adding multiple handlers
        handler = logging.FileHandler(f"{log_dir}/test_run.log", mode='w')
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
