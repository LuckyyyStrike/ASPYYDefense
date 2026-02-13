import logging
from engine import Engine

logging.basicConfig(
    filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

try:
    eng = Engine(10)
    eng.start()
except Exception as e:
    logger.error(e)
    raise
