from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200,unique=True)
    body = models.TextField()

    def __str__(self):
        return self.title