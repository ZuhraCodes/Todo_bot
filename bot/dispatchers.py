from telegram import Bot, Update
from telegram.ext import CallbackContext, Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from bot.handlers import commands, task
from bot import states

bot = Bot("7941363928:AAGWKu4SMr0j_UVDE4SQJWCSobcGDXXEh-Y")

dp = Dispatcher(bot, None, workers=1)

dp.add_handler(CommandHandler("start", commands.start))

dp.add_handler(ConversationHandler(
    entry_points=[
        MessageHandler(Filters.text("Create a new task"), commands.add_task)
    ],
    states={
        states.GET_TITLE: [
            MessageHandler(Filters.text, commands.add_task)
        ],
        states.GET_DESCRIPTION: [
            MessageHandler(Filters.text, task.add_task_description)
        ],
        states.SAVE: [
            MessageHandler(Filters.text, task.save_task)
        ]
    },
    fallbacks=[
        CommandHandler("start", commands.start)
    ]
))

dp.add_handler(MessageHandler(Filters.text("View my tasks") , task.view_task))
dp.add_handler(CallbackQueryHandler(task.get_task_by_id))
dp.add_handler(CallbackQueryHandler(task.get_task_actions)) 