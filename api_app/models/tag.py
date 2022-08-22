from django.db import models

from .account import Account

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'api_app'