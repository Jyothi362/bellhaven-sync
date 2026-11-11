import rapidfuzz
from crm.client import CRMClient

def normalize(name):
    return name.lower().replace("center", "").replace("of", "").strip()

def match_locations(scraped, crm_accounts):
    proposals = []

    for loc in scraped:
        best_match = None
        best_score = 0

        for acc in crm_accounts:
            if acc["city"] == loc["city"] and acc["state"] == loc["state"]:
                score = rapidfuzz.fuzz.ratio(normalize(loc["name"]), normalize(acc["name"]))
                if score > best_score:
                    best_score = score
                    best_match = acc

        if best_match and best_score >= 90:
            proposals.append({
                "type": "CONFIDENT_MATCH",
                "website": loc,
                "crm": best_match,
                "score": best_score
            })
        elif best_match and best_score >= 75:
            proposals.append({
                "type": "MATCH_NEEDS_FIX",
                "website": loc,
                "crm": best_match,
                "score": best_score
            })
        else:
            proposals.append({
                "type": "NEW_ACCOUNT_NEEDED",
                "website": loc,
                "crm": None,
                "score": best_score
            })

    return proposals
