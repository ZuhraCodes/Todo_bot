from telegram import Update
from telegram.ext import CallbackContext
from bot.models import TelegramUser
from bot.decorators import get_user
from bot import states
from todo.models import Task
from bot.keyboards import inlines, replies


@get_user
def add_task_description(update: Update, context:CallbackContext, user: TelegramUser):
    if not update and update.message.text:
        update.message.reply_text("Iltimos vazifangiz nomini to'g'ri kiriting: ")
        return states.GET_TITLE
    
    context.user_data["title"] = update.message.text
    
    update.message.reply_text("Vazifangi nimadan iborat ekanligini batafsil kiritng: ")
    return states.SAVE

@get_user
def save_task(update: Update, context:CallbackContext, user: TelegramUser):
    if not update and update.message.text:
        update.message.reply_text("Vazifangi nimadan iborat ekanligini to'g'ri kiritng:  ")
        return states.GET_DESCRIPTION
    
    context.user_data["description"] = update.message.text
    
    title = context.user_data.get("title")
    description = context.user_data.get("description")
    
    Task.objects.update_or_create(
        user=user,
        title=title,
        description=description
    )

    update.message.reply_text(f"Vazifangiz saqlandi!", reply_markup=replies.get_main_keyboard())
    return states.END

@get_user
def view_task(update: Update, context: CallbackContext, user: TelegramUser):
    tasks = Task.objects.filter(user=user)
    
    if not tasks:
        update.message.reply_text("Sizda saqlangan vazifangiz yo'q!")
        return
    
    text = "<b>Sizda saqlangan vazifalar:</b>\n"
    
    for task in tasks:
        text += f"{task.id}. {task.title}\n"
        
    update.message.reply_text(text, parse_mode="html", reply_markup=inlines.get_keyboards(tasks))
    
@get_user
def get_task_by_id(update: Update, context: CallbackContext, user:TelegramUser):
    task, task_id = str(update.callback_query.data).split("-")
    item = Task.objects.get(id=task_id)
    update.callback_query.message.delete()
    if task == "task":
        update.callback_query.message.reply_text(f"{item.id}. {item.title}\n{item.description}", parse_mode="html", reply_markup=inlines.get_task_id(task_id))
       
@get_user 
def get_task_actions(update: Update, context: CallbackContext, user: TelegramUser):
    action, todo_id = str(update.callback_query.data).split("-")
    item = Task.objects.get(id=todo_id)
    print(action)
    
    if action == "done":
        item.delete()
        tasks = Task.objects.filter(user=user)
    
    if action == "cancel":
        update.callback_query.message.delete()

    
    if action == "save":
        update.callback_query.message.reply_text("Sevimlilar ro'yxatiga saqlandi", reply_markup=replies.get_main_keyboard())
    
    return states.END
