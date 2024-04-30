import os


def get_database_url() -> str:
    return os.environ.get('DATABASEE_URL')
