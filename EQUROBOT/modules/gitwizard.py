from EQUROBOT import app
from pymongo import MongoClient
import hashlib
from pyrogram import filters

client = MongoClient('mongodb+srv://git:git@git.scvzxhw.mongodb.net')
db = client.mohio
collection = db.mohio

user_data = {}

@app.on_message(filters.command(["login"]))
async def login(_, message):
    try:
        username_msg = await app.ask(message.chat.id, "✅ **ENTER YOUR USERNAME**", reply_to_message_id=message.id, user_id=message.from_user.id)
        username = username_msg.text
        await username_msg.delete()

        user = collection.find_one({"username": username})
        if not user:
            return await message.reply_text("❌ Username Not Found in Database \n\n Register First at z.daxxteam.com")

        password_msg = await app.ask(message.chat.id, "✅ **ENTER YOUR PASSWORD**", reply_to_message_id=message.id, user_id=message.from_user.id)
        password = password_msg.text
        await password_msg.delete()

        if user['password'] == hashlib.sha256(password.encode('utf-8')).hexdigest():
            user_data[message.from_user.id] = {'username': username, 'password': password}
            await message.reply_text("✅ **Login Successful!**")
        else:
            await message.reply_text("❌ **Login Failed!**\n\nReason: `Password Incorrect`")
    except Exception as e:
        print(e)
        await message.reply_text(f"❌ **Login Failed**\n\nReason: {e}")

@app.on_message(filters.command(["fingerprint"]))
async def fingerprint(_, message):
    try:
        user_info = user_data.get(message.from_user.id)
        if not user_info:
            return await message.reply_text("❌ **Login Required**\n\nPlease login first to use this command.")

        username = user_info.get('username')
        password = user_info.get('password')

        user = collection.find_one({"username": username, "password": hashlib.sha256(password.encode('utf-8')).hexdigest()})
        if not user:
            return await message.reply_text("❌ **User Not Found in Database**")

        if len(message.text.split()) > 1:
            fingerprint = message.text.split(" ", 1)[1]
            collection.update_one({"username": username}, {"$push": {"fingerprint": fingerprint}})
            await message.reply_text("✅ **Fingerprint Updated**")
        else:
            fingerprint_list = user.get('fingerprint', [])
            if fingerprint_list:
                fingerprints = ', '.join(fingerprint_list)
                await message.reply_text(f"**Your Fingerprints:** `{fingerprints}`\n\nTo add a new fingerprint, provide it after the /fingerprint command.")
            else:
                await message.reply_text("❌ **No Fingerprints Set Yet**\n\nTo add a new fingerprint, provide it after the /fingerprint command.")
    except Exception as e:
        print(e)
        await message.reply_text(f"❌ **Failed to Update Fingerprint**\n\nReason: {e}")