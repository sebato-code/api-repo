import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

# VIOLACIÓN Estilo: console.log de debug残留（debug print）
print("DEBUG: FastAPI app starting...")

# VIOLACIÓN Estilo: nombre de función en snake_case en vez de camelCase
def get_user_by_id(user_id):
    return {"id": user_id, "name": "Test User"}

# VIOLACIÓN Técnica: SQL Injection
@app.get("/users")
async def list_users(username=None):
    db = psycopg2.connect(host="localhost", user="admin", password="secret123", dbname="test")
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return {"users": results}

# VIOLACIÓN Técnica: hardcoded credential
DATABASE_URL = "postgresql://admin:secret123@localhost:5432/mydb"

# VIOLACIÓN Estilo: import no utilizado
import smtplib  # no se usa en el archivo

@app.get("/")
def read_root():
    return {"Hello": "World"}
