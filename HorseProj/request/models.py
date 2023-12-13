from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Request(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class StableRequest(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    note= models.TextField(default="")
    
