from os import getenv
from dotenv import load_dotenv

load_dotenv()

""" General config """
# Set ENV to any value to use webhook instead of polling for bot. Must be set in prod environment.
ENV = getenv("ENV")

""" Telegram config """
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
BOTHOST = getenv("BOTHOST")  # only required in prod environment
