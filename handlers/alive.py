from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID, SUDO_USERS 




@Client.on_message(filters.command(["botcum", "alive"], [".", "/"]) & filters.user(OWNER_ID))
async def sahip(c: Client, m: Message):
    await m.reply("**Merhaba Sahip Bey ❤️**")


@Client.on_message(filters.command(["botcum", "alive"], [".", "/"]) & filters.user(SUDO_USERS))
async def admin(c: Client, m: Message):
    await m.reply("**Merhaba Yöneticim ❤️**")
