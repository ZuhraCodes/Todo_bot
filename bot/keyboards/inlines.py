from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboards(items):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=f"{item.title}", callback_data=f"task-{item.id}")] for item in items
        ]
    )
    
def get_task_id(task_id):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="Cancel", callback_data=f"cancel-{task_id}"),
             InlineKeyboardButton(text="Add to favourite", callback_data=f"save-{task_id}"),
             InlineKeyboardButton(text="Done", callback_data=f"done-{task_id}")
            ]
        ]
    )