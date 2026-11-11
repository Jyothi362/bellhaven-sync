import requests
from bs4 import BeautifulSoup

def scrape_bellhaven():
    url = "https://analyst-assessment-production.up.railway.app"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    locations = []

    # Example placeholder logic
    for card in soup.select(".community-card"):
        name = card.select_one(".name").text.strip()
        address = card.select_one(".address").text.strip()
        city = card.select_one(".city").text.strip()
        state = card.select_one(".state").text.strip()
        zip_code = card.select_one(".zip").text.strip()
        care = [c.text.strip() for c in card.select(".care-type")]

        locations.append({
            "name": name,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip_code,
            "care_offerings": care
        })

    return locations
