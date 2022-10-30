from email import message
from django.db import models

# Create your models here.

class Message(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()