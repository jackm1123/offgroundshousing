from django.db import models

class Listing(models.Model):
    """
    TODO: Add other listing fields, like location, square footage, etc.
    Don't forget to makemigrations.
    """
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def get_json(self):
        return dict_to_json(self.__dict__)

    def __str__(self):
        return str(self.name)

def dict_to_json(d):
    copy = d.copy()
    out = "{"

    for key in copy:
        out += '"' + key + '":'
        value = copy[key]
        if(type(value) == int):
            out += str(value) + ","
        else:
            out += '"' + str(value) + '",'

    out = out[:-1] # chop off last comma
    out += "}"
    return out
