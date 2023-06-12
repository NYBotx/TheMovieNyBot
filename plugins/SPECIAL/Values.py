from pyrogram import Client, filters, enums
import heroku3
from info import ADMINS, HRK_API, HRK_APP_NAME

heroku_conn = heroku3.from_key(HRK_API)
#apps = heroku_conn.apps()[HRK_APP_NAME]                             
app = heroku_conn.app(HRK_APP_NAME)



@Client.on_message(filters.command("setvar") & filters.user(ADMINS))
async def setvarrrz(bot, message):
    ms = await message.reply_text(text="<b>Proccesing...</b>")
    data = message.text        
    command, varname, value = data.split(" ")
    config = app.config()
    await ms.edit(text=f"<b>Completed..\nAdded New Varible In Heroku..\n\n Var Name : {varname}\nValue : {value}</b>")
    config[varname] = value
