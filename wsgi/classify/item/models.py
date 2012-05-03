from django.db import models

class Item(models.Model):
    added = models.DateTimeField()
    link = models.CharField(max_length=255)
    data = models.TextField()
