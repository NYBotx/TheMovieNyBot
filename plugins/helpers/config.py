import os
from os import environ
from dotenv import load_dotenv
load_dotenv()



API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
ADMINS = int(environ.get("ADMINS", ""))          
CAPTION = environ.get("CAPTION", "")

# for thumbnail ( back end is MrMKN brain 😉)
DOWNLOAD_LOCATION = "./DOWNLOADS"


# mdisk
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MDISK_API = os.environ.get("MDISK_API")
MDISK_CHANNEL = list(int(i.strip()) for i in os.environ.get("MDISK_CHANNEL").split(" ")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = bool(os.environ.get("FORWARD_MESSAGE"))
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("ADMINS") else []
SOURCE_CODE = "💕SHARE AND SUPPORT💕"
CHANNELS = bool(os.environ.get("CHANNELS"))


# attach


class Config(object):
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  #CHANNEL_USERNAME without '@'
  CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "bigmoviesworld")
