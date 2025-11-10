from .job_extractor import JobExtractor
from .company_extractor import CompanyExtractor
from utils.logger import Logger

class LinkedInParser:
    def __init__(self, settings, proxy=None):
        self.logger = Logger().get_logger()
        self.job_extractor = JobExtractor(proxy)
        self.company_extractor = CompanyExtractor(proxy)
        self.settings = settings

    def scrape_jobs(self, keyword: str):
        try:
            job_data = self.job_extractor.extract(keyword)
            for job in job_data:
                if "company_profile" in job:
                    company_data = self.company_extractor.extract(job["company_profile"])
                    job.update(company_data)
            return job_data
        except Exception as e:
            self.logger.error(f"Error scraping jobs for keyword '{keyword}': {e}")
            return []