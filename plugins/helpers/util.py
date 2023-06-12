import re
import requests
from pyrogram.types import MessageEntity
import ast
from pyrogram.types.list import List
import json
from plugins.helpers.config import MDISK_API
import re
from mdisky import Mdisk
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
MDISK_API = "tHRFNVu8CkjkdstzXNsp"
mdisk = Mdisk(MDISK_API)
####################  Mdisk  ####################

async def get_mdisk(link):
    url = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
    param = {'token': MDISK_API, 'link': link
             }
    res = requests.post(url, json=param)
    try:
        shareLink = res.json()
        link = shareLink["sharelink"]
    except:
        print(link, " is invalid")
    return link


async def replace_mdisk_link(text):
    links = re.findall(r'https?://mdisk.me[^\s]+', text)
    for link in links:
        try:
            mdisk_link = await get_mdisk(link)
            text = text.replace(link, mdisk_link)
        except:
            text = text.replace(link, text)

    return text


# caption entities


async def caption(caption_entities):
    x = []
    string = str(caption_entities)
    res = ast.literal_eval(string)
    try:
        for i in res:
            print(i)

            if "url" in i:
                print("Url")
                x.append(
                    MessageEntity(type=i["type"], offset=i["offset"], length=i["length"], url=await get_mdisk(i["url"])))
            elif "user" in i:
                print("user")
                x.append(MessageEntity(type=i["type"], offset=i["offset"], length=i["length"], url=i["user"]))
            else:
                print("others")
                x.append(MessageEntity(type=i["type"], offset=i["offset"], length=i["length"]))
          
        entities = List(x)
        
    except:
        entities = caption_entities
        
    return entities

async def main_convertor_handler(message:Message, type:str='mdisk', edit_caption:bool=False):
    caption = None

    if message.text:
        caption = message.text.html
    elif message.caption:
        caption = message.caption.html


    # Checking if the message has any link or not. If it doesn't have any link, it will return.
    if len(await extract_link(caption)) <=0 and not message.reply_markup:
        return

    # converting urls
    shortenedText = await replace_mdisk_link(caption)

    # converting reply_markup urls
    reply_markup = await reply_markup_handler(message, replace_mdisk_link)
        

    if message.text:

        if edit_caption:
            return await message.edit(shortenedText, disable_web_page_preview=True, reply_markup=reply_markup)

        return await message.reply(shortenedText, disable_web_page_preview=True, reply_markup=reply_markup, quote=True)

    elif message.media:
        medias = getattr(message, message.media.value)
        fileid = medias.file_id

        if edit_caption:
            return await message.edit_caption(shortenedText, reply_markup=reply_markup)

        if message.document:
            return await message.reply_document(fileid, caption=shortenedText, reply_markup=reply_markup, quote=True)

        
        elif message.photo:
            return await message.reply_photo(fileid, caption=shortenedText, reply_markup=reply_markup, quote=True)

async def extract_link(string):
    regex = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
    urls = re.findall(regex, string)
    return ["".join(x) for x in urls]



async def replace_mdisk_link(text):
    text = await mdisk.convert_from_text(text, True)
    return text

# Reply markup 
async def reply_markup_handler(message:Message, method_func):
    if message.reply_markup:
        reply_markup = json.loads(str(message.reply_markup))
        buttsons = []
        for markup in reply_markup["inline_keyboard"]:
            buttons = []
            for j in markup:
                text = j["text"]
                url = j["url"]
                url = await method_func(url)
                button = InlineKeyboardButton(text, url=url)
                buttons.append(button)
            buttsons.append(buttons)
        reply_markup = InlineKeyboardMarkup(buttsons)
        return reply_markup
