#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler
import requests


def curser(update,context):
  chat_id = update.message.chat_id
  req=requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=text')
  curse=req.content
  context.bot.send_message(chat_id=chat_id, text=curse.decode("utf-8"))


def main():
    updater = Updater('paste the bot token from botfather in telegram',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('curser',curser))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
