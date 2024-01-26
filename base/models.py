from django.db import models as md
from django.contrib.auth.models import User

class Topic(md.Model):
    name = md.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(md.Model):
    host = md.ForeignKey(User, on_delete=md.SET_NULL,null=True)
    topic = md.ForeignKey(Topic, on_delete=md.SET_NULL,null=True)
    name = md.CharField(max_length=200)
    description = md.TextField(null=True,blank=True)
    # participants = 
    updated = md.DateTimeField(auto_now=True)
    created = md.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(md.Model):
    user = md.ForeignKey(User, on_delete=md.CASCADE)
    room = md.ForeignKey(Room, on_delete=md.CASCADE)
    body = md.TextField()
    updated = md.DateTimeField(auto_now=True)
    created = md.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]