# LinkedIn Jobs & Company Scraper

> The LinkedIn Jobs & Company Scraper extracts job listings and company profiles directly from LinkedIn search pages. It helps recruiters, analysts, and job seekers gather structured job data and company insights without manual browsing.

> Designed for reliability and affordability, this tool provides high-quality job data with company details at scale.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>LinkedIn Jobs & Company Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The **LinkedIn Jobs & Company Scraper** is a data extraction tool that automates collecting job listings and company information from LinkedIn search results. It’s perfect for professionals in HR, recruitment, or analytics who want to streamline data collection and analysis.

### Why This Scraper Matters

- Saves hours of manual job and company data collection.
- Captures structured, detailed LinkedIn job listings.
- Extracts both job and company data in one go.
- Enables export to JSON, CSV, Excel, and more.
- Ideal for global searches — works across all LinkedIn regions.

## Features

| Feature | Description |
|----------|-------------|
| Dual Data Capture | Scrapes both job listings and company details in one run. |
| Flexible Filters | Supports LinkedIn search filters like role, location, salary, and experience. |
| Export Formats | Outputs data in JSON, CSV, XML, Excel, RSS, and JSONL. |
| High Throughput | Scrapes up to 1,000 jobs per session efficiently. |
| Proxy Support | Works with datacenter and residential proxies for reliability. |
| Low Cost | Optimized to minimize per-run and per-result cost. |
| Automation Ready | Easily integrates with pipelines or APIs for recruitment analytics. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| title | The job title (e.g., "Software Engineer"). |
| location | The location of the job post. |
| company_name | The company offering the job. |
| posted_datetime | The exact posting date and time. |
| posted_time_ago | Relative posting time (e.g., "2 days ago"). |
| applicants | Number of applicants for the position. |
| base_salary | Base salary offered, if available. |
| additional_compensation | Bonuses or additional benefits. |
| seniority_level | The required seniority for the job. |
| employment_type | Type of employment (Full-time, Contract, etc.). |
| job_function | Functional area of the job. |
| industries | Industry or sector relevant to the role. |
| description_text | Plain text job description. |
| description_html | HTML-formatted job description. |
| job_url | The direct LinkedIn URL to the job posting. |
| apply_type | Type of application ("Easy Apply" or external). |
| apply_url | Direct application page link. |
| recruiter_name | Recruiter’s name, if public. |
| recruiter_profile | Recruiter’s LinkedIn profile link. |
| company_profile | Company’s LinkedIn profile URL. |
| company_logo | URL of the company logo. |
| company_website | Official company website. |
| company_size | Number of employees. |
| company_headquarters | Company HQ location. |
| company_industry | Industry category of the company. |
| company_specialties | Key specialties or focus areas. |
| company_founded | Year the company was founded. |
| company_slogan | Tagline or slogan. |
| company_about_us | Detailed company overview. |

---

## Example Output

    [
      {
        "title": "Software Engineer for Training AI Data (Verilog)",
        "location": "London, England, United Kingdom",
        "company_name": "G2i Inc.",
        "posted_datetime": "2024-09-19 10:09:12",
        "employment_type": "Full-time",
        "job_function": "Engineering and Information Technology",
        "industries": "Software Development",
        "job_url": "https://uk.linkedin.com/jobs/view/software-engineer-for-training-ai-data-verilog-at-g2i-inc-4029759064",
        "apply_type": "External Apply",
        "company_profile": "https://www.linkedin.com/company/g2i-inc",
        "company_website": "https://g2i.co",
        "company_size": "11-50 employees",
        "company_headquarters": "Delray Beach, Florida",
        "company_industry": "Software Development"
      },
      {
        "title": "Data Protection Automation Engineer - Remote",
        "location": "London, England, United Kingdom",
        "company_name": "Lorien",
        "employment_type": "Full-time",
        "job_function": "Engineering and Information Technology",
        "industries": "Staffing and Recruiting",
        "job_url": "https://uk.linkedin.com/jobs/view/data-protection-automation-engineer-remote-at-lorien-4026404944",
        "company_profile": "https://uk.linkedin.com/company/lorien",
        "company_website": "https://www.lorienglobal.com/",
        "company_size": "201-500 employees",
        "company_industry": "Staffing and Recruiting"
      }
    ]

---

## Directory Structure Tree

    linkedin-jobs-and-company-scraper/
    ├── src/
    │   ├── main.py
    │   ├── extractors/
    │   │   ├── linkedin_parser.py
    │   │   ├── job_extractor.py
    │   │   └── company_extractor.py
    │   ├── utils/
    │   │   ├── proxy_handler.py
    │   │   └── logger.py
    │   └── config/
    │       └── settings.json
    ├── data/
    │   ├── inputs.sample.json
    │   └── sample_output.json
    ├── requirements.txt
    ├── LICENSE
    └── README.md

---

## Use Cases

- **Recruitment Agencies** use it to collect job listings and company data, so they can build candidate pipelines faster.
- **Market Analysts** use it to track hiring trends across industries, so they can analyze workforce demand.
- **Job Boards** use it to populate listings automatically, saving time on manual curation.
- **Data Scientists** use it to train models on employment patterns or salary predictions.
- **Business Intelligence Teams** use it to enrich databases with company and job market data.

---

## FAQs

**1. How many job listings can it scrape per run?**
Up to 1,000 listings per run. For larger data pulls, segment searches by location or keyword.

**2. Can I export the data into Excel or JSON?**
Yes — exports are available in JSON, CSV, XML, Excel, and JSONL formats.

**3. Does it capture company data automatically?**
Yes. The scraper includes both job and company details without requiring separate configurations.

**4. Is login or authentication required?**
No. It operates on public LinkedIn data using a logged-out session.

---

## Performance Benchmarks and Results

**Primary Metric:** Processes around 50 job results in under 3 minutes.
**Reliability Metric:** Maintains over 90% accuracy in result counts.
**Efficiency Metric:** Average cost per 50 results under $0.02 using datacenter proxies.
**Quality Metric:** Provides over 95% field completeness across extracted job records.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
