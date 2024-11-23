
# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "16874790"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "46aa49adca0f1d184eb2a2f4a48a1df9")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7052777665:AAGeBHb9WcfTEPenXjweljmGREanR8mUioY")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Cddfvbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "2070450796"))

EVAL = list(map(int, getenv("EVAL", "5852269476 7450003492 2070450796").split()))
# ------------------X------------------------------
DEEP_API = os.environ.get("DEEP_API", "96a36c8b-0a06-461a-bce3-851d5d997a60")
# ------------------------------------------------
LOGGER_ID = int(os.environ.get("LOGGER_ID", "-1002050666864"))
# ------------------------------------------------
GPT_API = os.environ.get("GPT_API", "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")
# ------------------------------------------------
DAXX_API = os.environ.get("DAXX_API", "5163c49d-b696-47f1-8cf9-")
# ------------------------------------------------
MONGO_DB = os.environ.get("CLONEDB", "mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.pom3ops.mongodb.net/?retryWrites=true&w=majority")
