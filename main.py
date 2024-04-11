import logging

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from config.config import TELEGRAM_TOKEN
from handlers.contact_handler import contact
from handlers.hello_handler import hello
from handlers.location_handler import location
from handlers.start_handler import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    hello_handler = CommandHandler('hello', hello)
    application.add_handler(hello_handler)

    location_handler = MessageHandler(filters.LOCATION, location)
    application.add_handler(location_handler)

    contact_handler = MessageHandler(filters.CONTACT, contact)
    application.add_handler(contact_handler)

    application.run_polling()
