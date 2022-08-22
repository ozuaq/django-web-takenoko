from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    communities = models.ManyToManyField('api_app.Community', blank=True)
    tags = models.ManyToManyField('api_app.Tag', blank=True)
    webpages = models.ManyToManyField('api_app.Webpage', blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'api_app'
    