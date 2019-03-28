from django.db import models

# Create your models here.

class User(models.Model):
    gender=(
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=129)
    password = models.CharField(max_length=256)
    gender = models.CharField(max_length=32,choices=gender)

    def __str__(self):
        return self.name