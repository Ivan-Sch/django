from django.db import models


# Create your models here.
class User(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)


class Post(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    date = models.DateTimeField("time published")
    message = models.CharField(max_length=500)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

