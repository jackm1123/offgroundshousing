from django.db import models
from datetime import datetime

class Listing(models.Model):

    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    description = models.TextField(default="")
    submission_date = models.DateTimeField(default=datetime.now, blank=True)
    LAUNDRY_CHOICES = [('L', 'Laundry'), ('N', 'No Laundry')]
    #The first element in each tuple is the value that will be stored in the database. The second element is displayed by the field’s form widget.
    laundry_info = models.CharField(choices=LAUNDRY_CHOICES, max_length=1, blank = False, default='N') # laundry required field
    square_footage = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    bedroom_num = models.IntegerField(default=0)
    phone_num = models.CharField(max_length=20, default=0)
    address = models.CharField(max_length=100, default="")
    OWNERSHIP_CHOICES = [('O', 'Owned'), ('A', 'Available')]
    ownership_info = models.CharField(choices=OWNERSHIP_CHOICES, max_length=1, blank = False, default='A') # status is required field




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
