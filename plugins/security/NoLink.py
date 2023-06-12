import os 
import pyrogram
from pyrogram import Client, filters
from info import BOT_TOKEN, API_ID, API_HASH
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
import asyncio
from info import SUPPORT_CHAT
import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery



import os
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


Bot = Client(
    "NoLink-BOT",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

              
      


@Client.on_message((filters.group) & filters.regex("@")  | filters.regex("t.me"))
async def nolink(bot,message):
        
	try:
                 
                buttons = [[
                    InlineKeyboardButton('sᴜʀᴘʀɪsᴇ', url='https://t.me/nasrani_update')
                ]]
                reply_markup = InlineKeyboardMarkup(buttons)
                k = await message.reply_sticker("CAACAgUAAx0CXPjPGAACAmVkAAHLpxQlUkQIctGPhN_l36xk9psAAlcJAAKTvwlU-kg3cws4x6geBA") 
                await asyncio.sleep(2)      
                k = await k.delete()
                hmm = await message.delete()
                return
                


	except:
		return
        




        
        

