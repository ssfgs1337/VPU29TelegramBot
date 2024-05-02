from telegram import Update
from telegram.ext import ConversationHandler, CommandHandler, ContextTypes

from handlers import BaseHandler

STATE_FIRST_NAME, STATE_LAST_NAME, STATE_PHONE_NUMBER = range(3)


class UserRegisterConversationHandler(BaseHandler):
    @classmethod
    def register(cls, app):
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('user_register', cls.user_register)],
            states={
                STATE_FIRST_NAME: [],
                STATE_LAST_NAME: [],
                STATE_PHONE_NUMBER: [],
            },
            fallbacks=[CommandHandler('exit_user_register', cls.exit_user_register)]
        )

        app.add_handler(conversation_handler)

    @staticmethod
    async def user_register(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

        return STATE_FIRST_NAME

    @staticmethod
    async def exit_user_register(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'Exit from conversation')

        return ConversationHandler.END