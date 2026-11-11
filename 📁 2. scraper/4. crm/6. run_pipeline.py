from scraper.scrape_bellhaven import scrape_bellhaven
from matcher.match_locations import match_locations
from crm.client import CRMClient
import json

def run():
    client = CRMClient("bh_CBgFHDiNlgmOaCjDpt2pQA")

    scraped = scrape_bellhaven()
    crm_accounts = client.list_accounts()

    proposals = match_locations(scraped, crm_accounts)

    for p in proposals:
        p["status"] = "pending"

    json.dump(proposals, open("proposals.json", "w"))

if __name__ == "__main__":
    run()
