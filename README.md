# 🔥 PyFirewall

**PyFirewall** is a lightweight, customizable firewall simulation project built using Flask. It controls access based on IP and port rules and supports dynamic rule updates via a secure REST API. Every request is logged and can be reviewed via a web interface.

## 🎯 Project Purpose

- Simulate firewall logic for educational or test environments
- Dynamically allow/block traffic using API-controlled rules
- Provide centralized logging and HTTP-based rule checking
- Learn about Flask, JSON-based rule processing, and minimal network control

---

## 🗂️ Folder Structure

```
PyFirewall/
│
├── firewall_server.py        # Flask-based main API server
├── rules.json                # JSON database for access rules
├── firewall.log              # Automatically generated log file
├── README.md                 # Project documentation (this file)
├── commands_kali.txt         # Example curl commands for Linux (Kali)
├── commands_windows.txt      # Example curl commands for Windows CMD
└── PyFirewall_Setup.txt      # Environment setup and preparation guide
```

📁 **Note:** After setting up the environment, a `venv/` folder will appear automatically. This folder should **not** be uploaded to GitHub (add to `.gitignore`).

---

## ⚙️ How to Run

1. Open terminal and navigate to project folder:
   ```bash
   cd PyFirewall
   ```

2. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Start the Flask server:
   ```bash
   python firewall_server.py
   ```

4. If successful, you will see:
   ```
   Running on http://127.0.0.1:5055
   ```

---

## 🔐 API Endpoints

| Endpoint        | Description                              | Method |
|----------------|------------------------------------------|--------|
| `/check`       | Check IP and port against rule list      | POST   |
| `/rules/update`| Add a new rule                           | POST   |
| `/rules/delete`| Remove an existing rule                  | POST   |
| `/logs`        | View logged activity in browser          | GET    |

> 🔐 Note: All POST requests require the `Authorization` header.

---

## 🧪 Test Examples

To test from other machines (e.g. Kali VM, Windows):

- Refer to `commands_kali.txt` for Linux curl examples
- Refer to `commands_windows.txt` for Windows curl examples

---

## 📄 Logging Feature

- Every access attempt and rule update is saved into a log file named `firewall.log`.
- This file is created automatically when the server starts and will store each request made to `/check`, `/rules/update`, or `/rules/delete`.

🧭 You can also **view logs in a browser** by visiting:
```
http://127.0.0.1:5055/logs
```
(or replace with your `FIREWALL_HOST` IP if testing remotely).

---

## 📦 Requirements

- Python 3.x
- Flask (`pip install flask`)
- (Recommended) Virtual environment via `venv`

---

## 📘 Setup Instructions

All terminal steps to set up the project are listed in **PyFirewall_Setup.txt**. Follow it line by line to create the folder, write necessary files, and activate the environment.

---

## ⚠️ Disclaimer

This is an **educational tool**. It is not intended for production use. Always use proper, audited firewalls in real environments.

---

## 👩‍💻 Developed By

**Bahtınur Ünal** — [GitHub: 0xnuorr](https://github.com/0xnuorr)