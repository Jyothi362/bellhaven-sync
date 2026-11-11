from flask import Flask, render_template, request, redirect
import json
from crm.client import CRMClient

app = Flask(__name__)
client = CRMClient("bh_CBgFHDiNlgmOaCjDpt2pQA")

@app.route("/")
def queue():
    proposals = json.load(open("proposals.json"))
    pending = [p for p in proposals if p["status"] == "pending"]
    return render_template("queue.html", proposals=pending)

@app.route("/proposal/<int:pid>")
def detail(pid):
    proposals = json.load(open("proposals.json"))
    proposal = proposals[pid]
    return render_template("detail.html", proposal=proposal)

@app.route("/approve/<int:pid>", methods=["POST"])
def approve(pid):
    proposals = json.load(open("proposals.json"))
    p = proposals[pid]

    if p["type"] == "NEW_ACCOUNT_NEEDED":
        client.create_account(p["website"])
    else:
        client.update_account(p["crm"]["id"], p["website"])

    p["status"] = "approved"
    json.dump(proposals, open("proposals.json", "w"))
    return redirect("/")

@app.route("/reject/<int:pid>", methods=["POST"])
def reject(pid):
    proposals = json.load(open("proposals.json"))
    proposals[pid]["status"] = "rejected"
    json.dump(proposals, open("proposals.json", "w"))
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
