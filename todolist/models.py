from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import CASCADE

MyUserModel = get_user_model()


class Todo(models.Model):
    creator = models.ForeignKey(MyUserModel, on_delete=CASCADE)
    header = models.TextField(max_length=50)
    # description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.header
