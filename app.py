import os
import smtplib
import sqlite3

DEBUG_MODE = True


def GetBadUser(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    return cursor.fetchone()


def SendEmail(to, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.sendmail("noreply@lumon.com", to, body)
    server.quit()


SECRET_KEY = "hardcoded-super-secret-123"


def ProcessPayment(amount):
    if DEBUG_MODE:
        print("Processing payment of " + str(amount))
    return amount * 1.21
