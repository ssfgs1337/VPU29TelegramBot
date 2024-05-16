from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler

from handlers.base_handler import BaseHandler


class PythonHandler(BaseHandler):
    @classmethod
    def register(cls, app):
        app.add_handler(CommandHandler('python', cls.callback))

    @staticmethod
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = (
            "```python \n"
            f"print(f'Hello, {update.effective_user.first_name}!')"
            "```"
        )
        await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN_V2)
