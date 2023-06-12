import asyncio
import os
import logging
from pyrogram import Client, filters, enums
from Script import script
from info import CHANNELS, ADMIN, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PM, ADMINS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)









@Client.on_message(filters.command("chat") & filters.text)
async def pm_text(client: Client, message):
    try:
        if message.from_user.id == ADMIN:
            await reply_text(client, message)
            return
        info = await client.get_users(user_ids=message.from_user.id)
        reference_id = int(message.chat.id)
        k = await client.send_message(
            chat_id=ADMIN,
            text=script.PM_TXT_ATT.format(reference_id, info.first_name, message.text),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
        
        await client.send_message(            
            chat_id=PM,
            text=script.PM_TXT_ATT.format(reference_id, info.first_name, message.text),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
        await asyncio.sleep(3000)
        await k.delete()

    


    except Exception as e:
        logger.exception(e)    



@Client.on_message(filters.private & filters.media)
async def reply_media(client: Client, message):   
    if message.from_user.id in ADMIN:
        await replay_media(bot, message)
        return
        info = await bot.get_users(user_ids=message.from_user.id)
        reference_id = int(message.chat.id)
        await bot.copy_message(
            chat_id=ADMIN,
            from_chat=message.chat.id,
            message_id=message.id,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                        ],
                        [
                            InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                            InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                        ]                            
                    ]
                )
            )        
    






@Client.on_message(filters.private & filters.user(ADMIN) & filters.text & filters.reply)
async def reply_text(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_message is not None:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
            await client.send_message(
                text=message.text,
                chat_id=int(reference_id),
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
    except Exception as e:
        logger.exception(e)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.media & filters.reply)
async def reply_media(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_message is not None:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
            await client.copy_message(
                chat_id=int(reference_id),
                from_chat_id=message.chat.id,
                message_id=message.id,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
    except Exception as e:
        logger.exception(e)




@Client.on_message(filters.private & filters.media & filters.reply)
async def reply_media(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_message is not None:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
            await client.copy_message(
                chat_id=ADMINS,
                from_chat_id=message.chat.id,
                message_id=message.id,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
    except Exception as e:
        logger.exception(e)

