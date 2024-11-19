from telegram import Update
from telegram.ext import CallbackContext
from bot.models import TelegramUser
from bot.decorators import get_user
from bot.keyboards import replies, inlines
from bot import states

@get_user
def start(update: Update, context:CallbackContext, user: TelegramUser):
    update.message.reply_text("Hello, I'm a Todo Bot!", reply_markup=replies.get_main_keyboard())
    
@get_user
def add_task(update: Update, context:CallbackContext, user: TelegramUser):
    update.message.reply_text("Vazifangiz nomini kiriting: ")
    return states.GET_DESCRIPTION
    
