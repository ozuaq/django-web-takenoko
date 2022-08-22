from django.db import models

from .account import Account

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=400)
    tags = models.ManyToManyField('api_app.Tag', blank=True)
    created_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'api_app'