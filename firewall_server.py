from flask import Flask, request, jsonify
from datetime import datetime
from threading import Thread
import json
import fnmatch

app = Flask(__name__)
rules_file = "rules.json"

# 📥 Load firewall rules from file
def load_rules():
    try:
        with open(rules_file, "r") as f:
            return json.load(f)
    except:
        return []

rules = load_rules()

# 🔐 Authorization middleware
@app.before_request
def check_auth():
    if request.path.startswith("/check") or request.path.startswith("/rules"):
        token = request.headers.get("Authorization")
        if token != "Bearer mysecuretoken123":
            return jsonify({"error": "Unauthorized"}), 401

# 🧠 Match incoming IP and port with existing rules (wildcard supported)
def check_rule(ip, port):
    for rule in rules:
        if fnmatch.fnmatch(ip, rule["ip"]) and port == rule["port"]:
            return rule["action"]
    return "allow"

# 🔍 Endpoint to check traffic against rules and log the result
@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    ip = data.get("ip")
    port = data.get("port")
    action = check_rule(ip, port)

    log_entry = f"{datetime.now().isoformat()} - IP: {ip}, Port: {port}, Result: {action.upper()}\n"
    with open("firewall.log", "a") as logfile:
        logfile.write(log_entry)

    return jsonify({"status": action})

# 📊 View last 50 log entries in a simple HTML format
@app.route("/logs", methods=["GET"])
def show_logs():
    try:
        with open("firewall.log", "r") as f:
            lines = f.readlines()[-50:]
    except FileNotFoundError:
        lines = ["Log file not found."]
    return "<h2>Firewall Log Records</h2><br>" + "<br>".join(lines[::-1])

# 📂 Return current rules as JSON
@app.route("/rules", methods=["GET"])
def get_rules():
    return jsonify(rules)

# ➕ Add a new rule via JSON
@app.route("/rules/update", methods=["POST"])
def update_rules():
    new_rule = request.get_json()
    rules.append(new_rule)
    with open(rules_file, "w") as f:
        json.dump(rules, f, indent=2)
    return jsonify({"message": "New rule added.", "rule": new_rule})

# ❌ Delete a rule by IP and port
@app.route("/rules/delete", methods=["POST"])
def delete_rule():
    global rules
    data = request.get_json()
    ip = data.get("ip")
    port = data.get("port")

    new_rules = [r for r in rules if not (r["ip"] == ip and r["port"] == port)]
    if len(new_rules) == len(rules):
        return jsonify({"message": "No matching rule found."}), 404

    rules = new_rules
    with open(rules_file, "w") as f:
        json.dump(rules, f, indent=2)
    return jsonify({"message": "Rule deleted.", "ip": ip, "port": port})

# 🚀 Start the Flask server in a separate thread
# ❗ If port 5055 is occupied, change it (e.g., to 5060 or 8000)
def run_app():
    app.run(host="0.0.0.0", port=5055)

Thread(target=run_app).start()
