from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
START_IMAGE = getenv("START_IMAGE", "https://telegra.ph//file/19a159c0927cb9d9379e9.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph//file/36a15fa7b75b0f424bda6.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/189fe27bff1207dd3eb85.jpg")
BOT_NAME = getenv("BOT_NAME", "Gece Kuşu")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME") 
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL") 
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
MONGODB_URL = getenv("MONGODB_URL")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
