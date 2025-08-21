from requests_html import HTMLSession 
import pandas as pd

url = "https://www.indeed.com/jobs?q=python+developer&l=India"

session = HTMLSession()
response = session.get(url)

response.html.render(timeout=20)

job_cards = response.html.find("div.job_seen_beacon")

jobs = []

for card in job_cards:
    title = card.find("h2", first=True).text if card.find("h2", first=True) else "N/A"
    company = card.find("span.companyName", first=True).text if card.find("span.companyName", first=True) else "N/A"
    location = card.find("div.companyLocation", first=True).text if card.find("div.companyLocation", first=True) else "N/A"

    jobs.append({
        "Title" : title,
        "Company" : company,
        "Location" : location
    })

df = pd.DataFrame(jobs)

df.to_csv("data/jobs.csv", index = False)


print(f"Scraped {len(jobs)} job listings")