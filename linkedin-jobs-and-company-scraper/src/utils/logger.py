import logging
import os

class Logger:
    def __init__(self, log_file="scraper.log"):
        os.makedirs("logs", exist_ok=True)
        self.logger = logging.getLogger("LinkedInScraper")
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(os.path.join("logs", log_file))
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger