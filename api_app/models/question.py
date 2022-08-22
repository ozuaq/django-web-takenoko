from django.db import models

from .issue import Issue
from .account import Account

# Create your models here.
class Question(models.Model):
    name = models.TextField()
    tags = models.ManyToManyField('api_app.Tag', blank=True)
    webpages = models.ManyToManyField('api_app.Webpage', blank=True)
    created_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'api_app'