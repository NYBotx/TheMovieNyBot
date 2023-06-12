import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType

import asyncio
from pyrogram import Client, filters, enums 
from plugins.helpers.admin_check import admin_check


@Client.on_message(filters.command(["purge", "purges"]))
async def purge(client, message):
    """ purge upto the replied message """
    if message.chat.type not in [ChatType.SUPERGROUP, ChatType.CHANNEL]:
        await message.delete()
        return

    status_message = await message.reply_text("...", quote=True)
    await message.delete()
    message_ids = []
    count_del_etion_s = 0

    if message.reply_to_message:
        for a_s_message_id in range(
            message.reply_to_message.id, message.id
        ):
            message_ids.append(a_s_message_id)
            if len(message_ids) == "1000":
                count_del_etion_s += await client.delete_messages(
                    chat_id=message.chat.id, message_ids=message_ids, revoke=True
                )
                message_ids = []
        if len(message_ids) > 0:
            count_del_etion_s += await client.delete_messages(
                chat_id=message.chat.id, message_ids=message_ids, revoke=True
            )

    await status_message.edit_text(f"deleted {count_del_etion_s} messages")
    await asyncio.sleep(5)
    await status_message.delete()






