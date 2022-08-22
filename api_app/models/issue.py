from django.db import models

from .community import Community
from .account import Account

# Create your models here.
class Issue(models.Model):
    name = models.CharField(max_length=600)
    created_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'api_app'