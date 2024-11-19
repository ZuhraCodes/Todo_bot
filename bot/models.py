from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Telegram User"
        verbose_name_plural = "Telegram Users"
        
    def __str__(self):
        return self.full_name