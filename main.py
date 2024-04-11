import logging

from telegram.ext import ApplicationBuilder

from config.config import TELEGRAM_TOKEN
from handlers.contact_handler import ContactHandler
from handlers.hello_handler import HelloHandler
from handlers.location_handler import LocationHandler
from handlers.start_handler import StartHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    StartHandler.register(app)
    ContactHandler.register(app)
    HelloHandler.register(app)
    LocationHandler.register(app)

    app.run_polling()
