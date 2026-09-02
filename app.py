import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("test.db")
    return conn


@app.route("/users")
def get_user():
    name = request.args.get("name", "")
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM users WHERE name = ?", (name,))
    return str(cursor.fetchall())


@app.route("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
