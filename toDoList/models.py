from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Task name:', max_length=200)


    def __str__(self):
        return self.title

