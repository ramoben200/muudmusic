import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command
from helpers.decorators import sudo_users_only
from helpers.dbchat import get_served_chats

from config import BOT_USERNAME as bn


@Client.on_message(command(["broadcast", f"broadcast@{bn}"]) & ~filters.edited)
@sudo_users_only
async def broadcast(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"✅  ɢʀᴜʙ ʏᴀʏɪɴɪ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**ᴋᴜʟʟᴀɴɪᴍ**:\n\n/broadcast (`ᴍᴇsᴀᴊ`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"✅ ɢʀᴜʙ ʏᴀʏɪɴɪ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n📌 {pin} pinleri ile")


@Client.on_message(command(["broadcast_pin", f"broadcast_pin@{bn}"]) & ~filters.edited)
@sudo_users_only
async def broadcast_pin(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"✅ Grupta yayın tamamlandı ."
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**ᴋᴜʟʟᴀɴɪᴍ**:\n\n/broadcast_pin (`ᴍᴇsᴀᴊ`) "
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            try:
                await m.pin(disable_notification=True)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"✅ Grupta yayın tamamlandı.\n📌 {pin} pinleri ile."
    )
