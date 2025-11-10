import random
from utils.logger import Logger

class ProxyHandler:
    def __init__(self, proxies):
        self.proxies = proxies
        self.logger = Logger().get_logger()

    def get_random_proxy(self):
        if not self.proxies:
            self.logger.info("No proxies configured. Proceeding without proxy.")
            return None
        proxy = random.choice(self.proxies)
        self.logger.info(f"Using proxy: {proxy}")
        return proxy