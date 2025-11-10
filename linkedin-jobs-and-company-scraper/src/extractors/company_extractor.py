import requests
from bs4 import BeautifulSoup
from utils.logger import Logger

class CompanyExtractor:
    def __init__(self, proxy=None):
        self.logger = Logger().get_logger()
        self.proxy = proxy

    def extract(self, company_url: str):
        self.logger.info(f"Fetching company details from {company_url}")
        headers = {"User-Agent": "Mozilla/5.0"}
        proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None

        try:
            response = requests.get(company_url, headers=headers, proxies=proxies, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            name = soup.find("h1", {"class": "top-card-layout__title"})
            size = soup.find("dd", {"class": "org-about-company-module__company-size-definition-text"})
            industry = soup.find("dd", {"class": "org-about-company-module__industry"})
            website = soup.find("a", {"class": "org-top-card-primary-actions__action"})

            company_info = {
                "company_name": name.text.strip() if name else None,
                "company_size": size.text.strip() if size else None,
                "company_industry": industry.text.strip() if industry else None,
                "company_website": website["href"] if website else None,
            }
            return company_info
        except Exception as e:
            self.logger.error(f"Failed to extract company data from '{company_url}': {e}")
            return {}