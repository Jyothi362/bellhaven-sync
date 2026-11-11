import requests

class CRMClient:
    def __init__(self, token):
        self.base = "https://analyst-assessment-production.up.railway.app/api/v1"
        self.headers = {"Authorization": f"Bearer {token}"}

    def list_accounts(self):
        return requests.get(f"{self.base}/accounts", headers=self.headers).json()

    def update_account(self, account_id, payload):
        return requests.patch(f"{self.base}/accounts/{account_id}", json=payload, headers=self.headers).json()

    def create_account(self, payload):
        return requests.post(f"{self.base}/accounts", json=payload, headers=self.headers).json()
