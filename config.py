from os import getenv

from dotenv import load_dotenv

load_dotenv()



class Vars:
    LOGGER = getenv("LOGGER", True)
    DB_URL = getenv("DB_URL") #get from deta.sh
    APP_KEY =  2992000
    OWNER_ID = 2107137268
    APP_HASH = "235b12e862d71234ea222082052822fd"
    TOKEN = getenv("TOKEN")
    HANDLER = "."