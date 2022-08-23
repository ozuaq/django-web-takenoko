from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    communities = models.ManyToManyField('api_app.Community', blank=True)
    tags = models.ManyToManyField('api_app.Tag', blank=True)
    webpages = models.ManyToManyField('api_app.Webpage', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'api_app'
    