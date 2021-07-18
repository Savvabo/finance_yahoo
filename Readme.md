# Run docker containers
docker compose up -d

# Navigate to scraper container
docker exec -it {finance_yahoo_scraper_1 container id} bash

# Run scraper for chosen company name
python3 scraper.py {company_name}
example: python3 scraper.py PD

# Query data on 0.0.0.0:5000 or some other ways like http requests