from django.db import models

class Listing(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return name
