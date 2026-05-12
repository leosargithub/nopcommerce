import logging

class log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\logs\\nopcommerce.logs", format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
             force= True,
            level=logging.INFO )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
