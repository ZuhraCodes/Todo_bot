import json
from telegram import Update
from django.http import JsonResponse
from bot.dispatchers import dp, bot

def message_handler(request):
    if request.method == "POST":
        update = Update.de_json(json.loads(request.body), bot)
        dp.process_update(update)   
    return JsonResponse({"result": "ok"})