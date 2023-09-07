from django.db import models
from django.contrib.auth.models import User
import datetime
import django.utils.timezone

# Create your models here.


# A basic model containing the members of the chat app:

class Members(models.Model):

    memberSince = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.username}"



#create the model for the chat room
class ChatRoom(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    nameslug = models.CharField(max_length=300)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdBy')
    def __str__(self):
        return f"{self.name}" 
    
    

class Messages(models.Model):
    message = models.CharField(max_length=9000)
    author = models.CharField(max_length=150)
    dateCreated = models.DateTimeField(default=datetime.datetime.now, blank=True)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='chatroom')

    def __str__(self):
        return f'{self.message}'
    


    
