import os


def GetEnvOrDefault(key, default):
    return os.getenv(key, default)


def BuildConnectionString(host, port):
    return "sqlite://" + host + ":" + str(port) + "/app.db"
