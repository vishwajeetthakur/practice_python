import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("TR")

a = (2,5)
logger.info("list is created")
b = 2*3
logger.info("b is calculated")
logger.info("value updated")
print("done logging")