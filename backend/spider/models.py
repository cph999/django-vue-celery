from django.db import models


class Widget(models.Model):
    name = models.CharField(max_length=140)


class TaskInfo(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    complete_time = models.DateTimeField()
    status = models.IntegerField()


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100)
    videos = models.CharField(max_length=1000)
    images = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    create_time = models.DateTimeField()
    userImage = models.CharField(max_length=1000)


class BookData(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_spu_number = models.CharField(max_length=50)
    book_price = models.FloatField()
    book_tips = models.CharField(max_length=200)
    book_outlet = models.CharField(max_length=100)
    comments_id = models.ManyToManyField(Comment)
