from .models import TelegramUser

def get_user(func):
    def wrapper(update, context, *args, **kwargs):
        if update and update.message:
            telegram_id = update.message.from_user.id,
            first_name = update.message.from_user.first_name,
            last_name = update.message.from_user.last_name,
            username = update.message.from_user.username
            
        elif update and update.callback_query:
            telegram_id = update.callback_query.message.from_user.id,
            first_name = update.callback_query.message.from_user.first_name,
            last_name = update.callback_query.message.from_user.last_name,
            username = update.callback_query.message.from_user.username
            
        user, created = TelegramUser.objects.update_or_create(
            telegram_id=telegram_id,
            defaults={
                "full_name": first_name,    
                "username": username
            }
        )
        return func(update, context, user)
    return wrapper
