from django.db import models
from bot.models import TelegramUser

class Task(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        
    def __str__(self) -> str:
        return self.title