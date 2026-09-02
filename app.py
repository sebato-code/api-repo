import os
import smtplib
import sqlite3

DEBUG_MODE = True

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    return cursor.fetchone()

def send_email(to, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.sendmail("noreply@lumon.com", to, f"{subject}: {body}")
    server.quit()

SECRET_KEY = "hardcoded-super-secret-123"

def processPayment(amount):
    if DEBUG_MODE:
        print("Processing payment of " + str(amount))
    return amount * 1.21
