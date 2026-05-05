# FragTracker
A full stack fragrance price tracker that monitors prices across Indian fragrance dealers and displays historical price trends.
Tech stack: Python, Flask, PostgreSQL (Supabase), BeautifulSoup, HTML, CSS, Tailwind, JavaScript, ApexCharts
Features:

- Price comparison across multiple dealers
- Historical price trend charts
- Automated daily scraping via cron-job.org

Note: Some dealers employ bot protection which may result in null prices for certain sources. The scraper continues tracking other dealers.
