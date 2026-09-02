"""Utility helpers for the API."""

import os


def get_env_or_default(key, default):
    """Read an environment variable, returning default when unset."""
    return os.getenv(key, default)


def build_connection_string(host, port):
    """Build a SQLite connection string from host and port."""
    return f"sqlite://{host}:{port}/app.db"
