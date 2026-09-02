"""Utility helpers for the API."""

import os


def GetEnvOrDefault(key, default):
    """Read an environment variable, returning default when unset."""
    return os.getenv(key, default)


def BuildConnectionString(host, port):
    """Build a connection string from host and port."""
    return "sqlite://" + host + ":" + str(port) + "/app.db"
