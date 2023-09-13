import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1087819304, #reza
    479344690, #ray
    1992087933, #xen
    1839010591, # amwang
    5569311686, # rewe
    5394259312, # vender
    1933872185, # shin
    1557184285, # kage
    1054295664, #KYNAN
    5170630278, #thnpiki
    1860375797, #uput
    6588255955, #arman01
    
]

KYNAN = list(map(int, os.getenv("KYNAN", "1807994668 1087819304 1054295664").split()))

API_ID = int(os.getenv("API_ID", "23855532"))

API_HASH = os.getenv("API_HASH", "3cc6eac0a9fbfe0b2b1da77f043cc9c9")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6358023244:AAHhsr6taVHa4_S8QOKj1qhgbIlEVz8Jr-E")

SESSION = os.getenv("SESSION", "")

OWNER_ID = int(os.getenv("OWNER_ID", "1087819304"))

USER_ID = list(map(int, os.getenv("USER_ID", "1087819304 1807994668").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1001967160939"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001675459127 -1001938303588 -1001861414061").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "27"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://zaza2zaza:77777@cluster0.lzftwjf.mongodb.net/?retryWrites=true&w=majority",
)
