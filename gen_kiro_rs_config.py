#!/usr/bin/env python3
"""从 kiro-cli 的 data.sqlite3 生成 kiro-rs 的 config.json 和 credentials.json"""

import sqlite3, json, os, secrets

DB_PATH = os.path.expanduser("~/.local/share/kiro-cli/data.sqlite3")
OUTPUT_DIR = os.path.expanduser("~/kiro-rs-config")

os.makedirs(OUTPUT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

auth = {}
cur.execute("SELECT key, value FROM auth_kv")
for key, value in cur.fetchall():
    auth[key] = json.loads(value)

conn.close()

token = auth.get("kirocli:social:token", {})
device = auth.get("kirocli:odic:device-registration", {})

# --- config.json ---
config = {
    "host": "0.0.0.0",
    "port": 8990,
    "apiKey": f"sk-kiro-rs-{secrets.token_hex(16)}",
    "region": device.get("region", "us-east-1"),
}

with open(os.path.join(OUTPUT_DIR, "config.json"), "w") as f:
    json.dump(config, f, indent=2)

# --- credentials.json ---
cred = {
    "accessToken": token.get("access_token", ""),
    "refreshToken": token.get("refresh_token", ""),
    "profileArn": token.get("profile_arn", ""),
    "expiresAt": token.get("expires_at", ""),
    "authMethod": "social" if token.get("provider") else "idc",
}

if cred["authMethod"] == "idc":
    cred["clientId"] = device.get("client_id", "")
    cred["clientSecret"] = device.get("client_secret", "")

with open(os.path.join(OUTPUT_DIR, "credentials.json"), "w") as f:
    json.dump(cred, f, indent=2)

print(f"apiKey: {config['apiKey']}")
print(f"输出目录: {OUTPUT_DIR}")
