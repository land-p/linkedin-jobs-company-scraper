import requests
from bs4 import BeautifulSoup
from utils.logger import Logger

class JobExtractor:
    def __init__(self, proxy=None):
        self.logger = Logger().get_logger()
        self.proxy = proxy

    def extract(self, keyword: str):
        base_url = f"https://www.linkedin.com/jobs/search?keywords={keyword}"
        self.logger.info(f"Fetching jobs from {base_url}")
        headers = {"User-Agent": "Mozilla/5.0"}
        proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None

        try:
            response = requests.get(base_url, headers=headers, proxies=proxies, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            job_cards = soup.find_all("div", {"class": "base-card"})
            results = []

            for job in job_cards:
                title_tag = job.find("h3", {"class": "base-search-card__title"})
                company_tag = job.find("h4", {"class": "base-search-card__subtitle"})
                location_tag = job.find("span", {"class": "job-search-card__location"})
                link_tag = job.find("a", {"class": "base-card__full-link"})

                job_info = {
                    "title": title_tag.text.strip() if title_tag else None,
                    "company_name": company_tag.text.strip() if company_tag else None,
                    "location": location_tag.text.strip() if location_tag else None,
                    "job_url": link_tag["href"] if link_tag else None,
                }
                results.append(job_info)

            self.logger.info(f"Found {len(results)} jobs for keyword '{keyword}'")
            return results
        except Exception as e:
            self.logger.error(f"Failed to extract jobs for '{keyword}': {e}")
            return []