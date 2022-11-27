from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    realName = models.CharField(max_length=10)
    age = models.IntegerField()
    height = models.FloatField()


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username', 'realName', 'age', 'height', 'url', 'pk')

