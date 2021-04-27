from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from apidata import get_headlines


# Getting News Data

number = 0


# function to handle the /start command
def start(update, context):
    update.message.reply_text('Hi there, \n 1. set the number of headlines you wish to recieve by /set_number \n 2. Type /news to recieve 5 headlines')

# function to handle the /help command
def help(update, context):
    update.message.reply_text('Hi there, \n 1. set the number of headlines you wish to recieve by /set_number \n 2. Type /news to recieve 5 headlines')


def set_number(update, context):
    update.message.reply_text('currently not working')

def news(update, context):
    number=0
    if number==0:
        update.message.reply_text('using default value as 5')
        try:
          articles = get_headline("5")
          # Getting news for 5 articles
          article_string="\n Daily Headlines \n"
          for n in articles:
            name = n['source']['name']
            author = n['author']
            title = n['title']
            url = n['url']
            article_string += f'title:{title} \n author:{author} \n url:{url} \n Provided By{name} \n -------- \n'

          update.message.reply_text(f'{article_string}')
        except :
          print(error) 
          update.message.reply_text('📡 Nothing Check your internet 📡')

    else:
        update.message.reply_text('📡 Nothing Check your internet 📡')

# function to handle errors occured in the dispatcher 
def error(update, context):
    update.message.reply_text('Ummm I think something is not fine')

# function to handle normal text 
def text(update, context):
    text_received = update.message.text

def main():
  TOKEN = os.getenv('BOT_TOKEN') 

    # create the updater, that will automatically create also a dispatcher and a queue to 
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("set_number", set_number))
    dispatcher.add_handler(CommandHandler("news", news))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
