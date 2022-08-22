from django.db import models

from .question import Question
from .account import Account

# Create your models here.
class Message(models.Model):
    name = models.TextField()
    webpages = models.ManyToManyField('api_app.Webpage', blank=True)
    created_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'api_app'