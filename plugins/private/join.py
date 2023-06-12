from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import random
import os
Doctor=Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
ALL_PIC = [
 "https://telegra.ph/file/d6693066f82ed4079c528.jpg",
 "https://telegra.ph/file/65a9972e351b02640d0f4.jpg"
 ]
START_MESSAGE ="""
H𝙻𝙾 {} 𝙱𝚁𝙾𝙷
ᗰ𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href='https://t.me/pyogram_bot'>ᴅᴀᴠᴏᴏᴅ ɪʙʀᴀʜɪᴍ⚡️</a>
𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙸𝚂 𝙵𝙸𝚁𝚂𝚃 𝙾𝚆𝙽 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙱𝙾𝚃 𝙾𝙵 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 𝚂𝙾 𝚃𝙷𝙴 𝙱𝙾𝚃 𝙸𝚂 𝙾𝙽 𝚃𝙷𝙴 𝚆𝙾𝚁𝙺𝚂𝙷𝙾𝙿 𝙾𝙽 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙵𝙾𝚁 𝚄𝙿𝙳𝙰𝚃𝙸𝙽𝙶 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝚂𝙾 𝙿𝙻𝙴𝙰𝚉𝙴 𝚆𝙰𝙸𝚃 𝙺𝙸𝙽𝙳𝙵𝚄𝙻𝙻𝚈...
"""
@Client.on_message(filters.command("ads")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=START_MESSAGE.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("STARTES", callback_data="start")
            ]]
            )
        )



        



