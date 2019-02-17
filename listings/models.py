from django.db import models

class Listing(models.Model):
    """
    TODO: Add other listing fields, like location, square footage, etc.
    Don't forget to makemigrations.
    """
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
