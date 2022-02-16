from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

Hacker=Client(
      "PyrogramBOT",
      bot_token="5166763908:AAGvTJHggdiJJ9A_iVc87Au5cnhLykihcGU",
      api_id="9024035",
api_hash="89b2d2c0120a5ae9e41b9891fdcc3f8f"
)

ALL_PIC = [
"https://telegra.ph/file/5f8509f8c3e343b1997fc.jpg",
"https://telegra.ph/file/fe162cec8e20318af1adb.jpg",
"https://telegra.ph/file/198d183c95258d6f73b79.jpg",
"https://telegra.ph/file/c34d09d42700a8a85edf2.jpg"
]

@Hacker.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""Hi {message.from_user.mention} My name is <a href=http://t.me/FSpyrogrambot>Pyrogram bot</a>, bro my owner is under my developing me, so wait until he finishes all my work""",
        reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("🔊channel🔊", url="https://t.me/Filmspoterchannel"),
          InlineKeyboardButton ("💬group💬", url="https://t.me/Filmspoters"),
          ],[
          InlineKeyboardButton ("🧑‍💻Developer 🧑‍💻", url="https://t.me/Hacker_A10"),
        ],[
          )

          (




Hacker.on_message(filters.command("sticker

Hacker.on_message(filters.command("sticker"))

Hacker.on_message(filters.command("sticker"))
async def sticker(bot, message):
        await message.reply_sticker(

sticker=CAACAgEAAxkBAAEB0jliAAHkGVBsrlTJTwYAAVaq1TXFpCluAAIZAgACxIbYRbYTWYpNytmLHgQ

sticker=CAACAgEAAxkBAAEB02diAiPeNsOpeB1lfF25Fsibw9mdQAACjgEAAsN2aUYhFV4FsuFCkx4E




Hacker.run()
