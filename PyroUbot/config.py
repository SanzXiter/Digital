import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "9999"))

DEVS = list(map(int, os.getenv("DEVS", "7118977824").split()))

API_ID = int(os.getenv("API_ID", "24723685"))

API_HASH = os.getenv("API_HASH", "23fae0b610095d2efeb6d8494b5cf81c")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7701110910:AAEMvR1RZNTlFJbDwtuCCAN0RUfAtO-iFvQ")

OWNER_ID = int(os.getenv("OWNER_ID", "7118977824"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002399953106").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://stokressfixzzjb:sanz@321@sanz.kdylzvr.mongodb.net/?retryWrites=true&w=majority&appName=sanz")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))

USER_GROUP = os.getenv("USER_GROUP", "@ATTACKSANZ")
