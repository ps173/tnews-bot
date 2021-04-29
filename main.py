import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from apidata import get_headlines,search_headline,get_articles_as_text

load_dotenv()

# Getting News Data
headlinesNum = ""

helptext = """
  Hi there 👋,
  I am tbot and I provide news to you

  1. Type /news **category** to recieve top 5 headlines of that category (change every hour)
     categories : (business entertainment general health science sports technology)
 
  for example : /news technology

  2. Type /search **search query** to search for a headline
"""

def start(update, context):
    update.message.reply_text(helptext)

def help(update, context):
    update.message.reply_text(helptext)


def search_for_news(update, context):
    search_q = update.message.text
    newsarr = search_headline(search_q)
    reply_news = get_articles_as_text(newsarr)
    update.message.reply_text(f'{reply_news}')

def news(update, context):
    category_q = update.message.text
    if "/news" in category_q:
      category_q = category_q[5:]
      print(category_q)
      try:
        headlineArr = get_headlines(category_q,"5")
        reply_news = get_articles_as_text(headlineArr)
        update.message.reply_text(f'{reply_news}')
      except :
        print(error) 
        update.message.reply_text('📡 Nothing Check your internet 📡')


def error(update, context):
    update.message.reply_text('Ummm I think something is not fine')

def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'did you say {text_received}')

def main():
  TOKEN = os.getenv('BOT_TOKEN') 

  updater = Updater(TOKEN, use_context=True)
  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("help", help))
  dispatcher.add_handler(CommandHandler("search", search_for_news))
  dispatcher.add_handler(CommandHandler("news", news))

  dispatcher.add_handler(MessageHandler(Filters.text, text))

  dispatcher.add_error_handler(error)

  updater.start_polling()

  updater.idle()

if __name__ == '__main__':
    main()
