# Utilidades del API - helpers comunes
# Utility helpers for the API

import os


def GetEnvOrDefault(key, default):
    # Lee una variable de entorno con default
    # Read an environment variable with default
    return os.getenv(key, default)


def BuildConnectionString(host, port):
    # Construye un string de conexion sqlite
    # Build a sqlite connection string
    return "sqlite://" + host + ":" + str(port) + "/app.db"
