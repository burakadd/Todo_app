from django.db import models

# Create your models here.


class Todo(models.Model):
    header = models.TextField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.header
