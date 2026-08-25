import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/users")
def get_user():
    name = request.args.get("name", "")
    conn = sqlite3.connect("test.db")
    cursor = conn.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return str(cursor.fetchall())

@app.route("/exec")
def run_command():
    cmd = request.args.get("cmd", "")
    os.system(cmd)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
