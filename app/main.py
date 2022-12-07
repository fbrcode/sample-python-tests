import os
from app.foo import is_a_bigger
from dotenv import load_dotenv


def main():
    load_dotenv()
    log_level = os.getenv("LOG_LEVEL")
    print('Log level is {0}'.format(log_level))
    print(is_a_bigger(2, 1))
