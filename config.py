from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 29232955))
API_HASH = getenv("API_HASH", "db98eba424dfb1755f72db5fa71785e1")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "6713421664"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "suppooorttt")
UPDATE_CHNL = getenv("UPDATE_CHNL", "suppooorttt")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Mr_nobi_1")

# Random Start Images
IMG = [
    "https://graph.org/file/2c30aed72f9553fcedbfa.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",

]

EMOJIOS = [
    "🤭",
    
]
