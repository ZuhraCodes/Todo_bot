from telegram import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    keyboards = [
        [
            KeyboardButton("Create a new task"),
            KeyboardButton("View my tasks"),
            KeyboardButton("Favourites")
        ]
    ]
    return ReplyKeyboardMarkup(keyboards, resize_keyboard=True)