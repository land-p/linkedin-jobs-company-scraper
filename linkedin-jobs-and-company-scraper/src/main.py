import json
import os
from extractors.linkedin_parser import LinkedInParser
from utils.logger import Logger
from utils.proxy_handler import ProxyHandler
from config.settings import load_settings

def main():
    logger = Logger().get_logger()
    settings = load_settings()

    input_file = os.path.join("data", "inputs.sample.json")
    output_file = os.path.join("data", "sample_output.json")

    logger.info("Starting LinkedIn Jobs & Company Scraper")

    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        search_terms = json.load(f)

    proxies = ProxyHandler(settings.get("proxies", [])).get_random_proxy()
    parser = LinkedInParser(settings, proxies)

    all_results = []
    for term in search_terms.get("search_terms", []):
        logger.info(f"Scraping for term: {term}")
        jobs = parser.scrape_jobs(term)
        all_results.extend(jobs)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)

    logger.info(f"Scraping completed. Results saved to {output_file}")

if __name__ == "__main__":
    main()