from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    task = models.TextField()

