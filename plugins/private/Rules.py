
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
# from pyrogram.types import CallbackQuery
import random
import os
from info import SP
from Script import script
import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import BR_IMDB_TEMPLATE, PROTECT_CONTENT, AUTH_CHANNEL, BATCH_LINK, ADMINS, LOG_CHANNEL
from utils import extract_user, get_file_id, get_poster, last_online
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.ia_filterdb import Media, get_file_details, get_search_results, get_bad_files
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
from info import IMDB









Muhammed = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

ALL_PIC = [
 "https://telegra.ph/file/d6693066f82ed4079c528.jpg",
 "https://telegra.ph/file/65a9972e351b02640d0f4.jpg"
 ]



START_MESSAGE = """
𝐇𝐞𝐥𝐥𝐨 <a href='tg://settings'>𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮⚡️</a>

🔰𝐇𝐨𝐰 𝐓𝐨 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐀𝐧𝐝 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐢𝐥𝐞 
<a href='https://telegra.ph/file/b6bbdff439c375f18866d.mp4'>📤𝐖𝐚𝐭𝐜𝐡 𝐕𝐢𝐝𝐞𝐨📤</a> \n

<i>📌ഏതു മൂവി ആണോ വേണ്ടത് അത് സ്പെല്ലിങ് തെറ്റാതെ ഗ്രൂപ്പിൽ ചോദിച്ചാൽ മാത്രമേ കിട്ടുകയുള്ളു...!! \n\n
സിനിമകൾ/സീരിസുകൾ ലഭിക്കാൻ പേര് മാത്രം അയച്ചാൽ മതി, അങ്ങനെ കിട്ടിയില്ലെങ്കിൽ വർഷം/സീസൺ(s)+എപ്പിസോഡ്(E)
കൂടി ചേർത്ത് അയക്കുക, അതിന്റെ കൂടെ ഉണ്ടോ? കിട്ടുമോ? തരോ ഇങ്ങനെയുള്ളതോ അല്ലെങ്കിൽ വേറെ ഭാഷയോ ചേർക്കേണ്ടതില്ല.</i>

𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :-

𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 ✅
𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 𝟐𝟎𝟐𝟑 ✅
𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 𝐌𝐚𝐥𝐚𝐲𝐚𝐥𝐚𝐦 ✅
𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 𝐌𝐚𝐥𝐚𝐲𝐚𝐥𝐚𝐦 𝐌𝐨𝐯𝐢𝐞 𝐍𝐞𝐰 ❌️
𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 𝐍𝐞𝐰 𝐌𝐨𝐯𝐢𝐞 ❌️
𝐀𝐯𝐞𝐧𝐠𝐞𝐫𝐬 𝐄𝐧𝐝𝐠𝐚𝐦𝐞 ✅
𝐀𝐯𝐞𝐧𝐠𝐞𝐫𝐬:𝐄𝐧𝐝𝐠𝐚𝐦𝐞 ❌️

𝐑𝐮𝐥𝐞𝐬 𝐀𝐧𝐝 𝐁𝐨𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 <a href='http://telegra.ph/Minnal-murali-03-06-12'>𝐂𝐥𝐢𝐜𝐤⚡️</a>

<i>📌നിങ്ങൾ റിക്വസ്റ്റ് ചെയ്ത മൂവി കിട്ടിയില്ലെങ്കിൽ വൈകാതെ തന്നെ ആഡ് ചെയ്യുന്നതായിരിക്കും..</i> 

🍿𝐃𝐨𝐧'𝐭 𝐀𝐤𝐬 𝐓𝐡𝐞𝐚𝐭𝐫𝐞 🎭 𝐑𝐞𝐥𝐞𝐚𝐬𝐞𝐝 𝐌𝐨𝐯𝐢𝐞𝐬
𝐏𝐥𝐞𝐚𝐬𝐞 𝐝𝐨 𝐧𝐨𝐭 𝐬𝐭𝐚𝐲 𝐢𝐧 𝐭𝐡𝐢𝐬 𝐠𝐫𝐨𝐮𝐩 𝐛𝐲 𝐚𝐬𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐚𝐧 𝐮𝐧𝐫𝐞𝐥𝐞𝐚𝐬𝐞𝐝 𝐟𝐢𝐥𝐦.  𝐘𝐨𝐮 𝐰𝐢𝐥𝐥 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐚 𝐰𝐚𝐫𝐧𝐢𝐧𝐠 𝐢𝐟 𝐲𝐨𝐮 𝐚𝐬𝐤.\n\n
𝐘𝐨𝐮 𝐖𝐢𝐥𝐥 𝐆𝐞𝐭 𝐅𝐢𝐫𝐞 🔥,𝐈𝐟 𝐘𝐨𝐮 𝐀𝐬𝐤𝐢𝐧𝐠 𝐍𝐨𝐧 𝐑𝐞𝐥𝐞𝐚𝐬𝐞𝐝 𝐌𝐨𝐯𝐢𝐞.

வெளியிடப்படாத படம் கேட்டு தயவுசெய்து இந்த குழுவில் தங்க வேண்டாம்.  நீங்கள் கேட்டால் எச்சரிக்கையைப் பெறுவீர்கள். \n

𝐎𝐰𝐧𝐞𝐫 𝐍𝐚𝐦𝐞 :- {}
𝐆𝐫𝐨𝐮𝐩 𝐍𝐚𝐦𝐞 :- {}
"""
UP_MESSAGE = """
{} {} 𝐌𝐨𝐯𝐢𝐞 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩
"""







# @Client.on_callback_query()
# async def callback(bot: Client, query: CallbackQuery):
#     if query.data== "r":
#         await query.message.edit(
#             text=f"ok da"
#         )





@Client.on_message(filters.private & filters.text & filters.user(ADMINS) & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    imdb = await get_poster(content) if IMDB else None
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
#    if user_id in ADMINS: return # ignore admins
    
    
    try:
            buttons = [[
                InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/nasrani_update'),
                InlineKeyboardButton("𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞", url=f"https://telegram.me/{temp.U_NAME}?start"),
                InlineKeyboardButton('𝐋𝐞𝐭𝐞𝐬𝐭 𝐓𝐫𝐲', url=(BATCH_LINK))      
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply_photo(photo=imdb.get('poster'), caption=f"𝐇𝐞𝐲 {content} 𝐌𝐨𝐯𝐢𝐞 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩...\n\n🏷𝐓𝐢𝐭𝐥𝐞 :  {imdb.get('title')}\n\n🎭 Genres: {imdb.get('genres')}\n\n🌟 𝐑𝐚𝐭𝐢𝐧𝐠 : {imdb.get('rating')}\n\n☀️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬 : {imdb.get('languages')}\n\n📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞 : {imdb.get('runtime')}\n\n📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {imdb.get('year')}\n\n🎛 𝐂𝐨𝐮𝐧𝐭𝐫𝐢𝐞𝐬 : {imdb.get('countries')}\n\n{imdb.get('title')} എന്ന സിനിമ വേണമെങ്കിൽ ഇപ്പോൾ തന്നെ കാണുന്ന ബട്ടൺ ക്ലിക്ക് ചെയ്ത് ഗ്രൂപ്പിൽ ജോയിൻ ജോയിൻ ചെയ്യൂ..\n\n𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ©𝐍𝐚𝐬𝐫𝐚𝐧𝐢 𝐔𝐩𝐝𝐚𝐭𝐞",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
            )
                                      
    except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            buttons = [[
                InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/nasrani_update'),
                InlineKeyboardButton("𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞", url=f"https://telegram.me/{temp.U_NAME}?start"),
                InlineKeyboardButton('𝐋𝐞𝐭𝐞𝐬𝐭 𝐓𝐫𝐲', url=(BATCH_LINK))           
            ]]
            hmm = await message.reply_photo(photo=poster, caption=f"𝐇𝐞𝐲 {content} 𝐌𝐨𝐯𝐢𝐞 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩...\n\n🏷𝐓𝐢𝐭𝐥𝐞 :  {imdb.get('title')}\n\n🎭 Genres: {imdb.get('genres')}\n\n🌟 𝐑𝐚𝐭𝐢𝐧𝐠 : {imdb.get('rating')}\n\n☀️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬 : {imdb.get('languages')}\n\n📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞 : {imdb.get('runtime')}\n\n📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {imdb.get('year')}\n\n🎛 𝐂𝐨𝐮𝐧𝐭𝐫𝐢𝐞𝐬 : {imdb.get('countries')}\n\n{imdb.get('title')} എന്ന സിനിമ വേണമെങ്കിൽ ഇപ്പോൾ തന്നെ കാണുന്ന ബട്ടൺ ക്ലിക്ക് ചെയ്ത് ഗ്രൂപ്പിൽ ജോയിൻ ജോയിൻ ചെയ്യൂ..\n\n𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ©𝐍𝐚𝐬𝐫𝐚𝐧𝐢 𝐔𝐩𝐝𝐚𝐭𝐞",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
            )
    except Exception as e:
        logger.exception(e)




