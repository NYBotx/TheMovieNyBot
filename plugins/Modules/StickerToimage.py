import imghdr, os
from asyncio import gather
from traceback import format_exc
from pyrogram import filters, Client
from pyrogram.types import *
from pyrogram.errors import *
# from utils.files import *
# from utils.stickerset import *
    
MAX_STICKERS = (120)  # would be better if we could fetch this limit directly from telegram
SUPPORTED_TYPES = ["jpeg", "png", "webp", "gif", "mp4"]


@Client.on_message(filters.command("get_sticker"))
async def sticker_image(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.reply("Reply to a sticker.")

    if not r.sticker:
        return await message.reply("Reply to a sticker.")

    m = await message.reply("Sending..")
    f = await r.download(f"{r.sticker.file_unique_id}.png")

    await gather(
        *[
            message.reply_photo(f),
            message.reply_document(f),
        ]
    )

    await m.delete()
    os.remove(f)
