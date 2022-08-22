from unicodedata import name
from django.db import models

from .account import Account

# Create your models here.
class Webpage(models.Model):
    name = models.CharField(max_length=400)
    url = models.URLField()
    created_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'api_app'