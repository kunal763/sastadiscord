from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Room(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100)
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    description=models.CharField(max_length=200)
    participant=models.ManyToManyField(User,related_name='participant',blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']
    def __str__(self):
        return self.name

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    text=models.TextField()
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']
    def __str__(self):
        return self.text[0:15]



