from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from geopy import Nominatim
import geopy




class Listing(models.Model):

    name = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    description = models.TextField(default="")
    LAUNDRY_CHOICES = [('L', 'Laundry'), ('N', 'No Laundry')]
    #The first element in each tuple is the value that will be stored in the database. The second element is displayed by the field’s form widget.
    laundry_info = models.CharField(choices=LAUNDRY_CHOICES, max_length=1, blank = False, default='N') # laundry required field
    PARKING_CHOICES = [('P', 'Parking'), ('N', 'No Parking')]
    parking_info = models.CharField(choices=PARKING_CHOICES, max_length=1, blank = False, default='N') # laundry required field
    square_footage = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    bedroom_num = models.IntegerField(default=0)
    phone_num = models.CharField(max_length=20, default=0)
    address = models.CharField(max_length=100, default="")
    OWNERSHIP_CHOICES = [('O', 'Owned'), ('A', 'Available')]
    ownership_info = models.CharField(choices=OWNERSHIP_CHOICES, max_length=1, blank = False, default='A') # status is required field
    submission_date = models.DateTimeField(default=timezone.now, blank=True)

    pictures = models.TextField(default="")
    # latitude = models.DecimalField(max_digits=6, decimal_places=3, default=38.034)
    # longitude = models.DecimalField(max_digits=6, decimal_places=3, default=78.508)

    active = models.BooleanField(default=True) #change to true for testing, will be made default false later
    favorite = models.BooleanField(default=False) #need to go find one.
    user_profile_list = models.ManyToManyField('users.UserProfile', blank=True, related_name='user_favourite')
    user_list = models.ManyToManyField(User, blank=True, related_name='user_favourite')

    num_ratings = models.IntegerField(default=0)

    cached_latitude = models.FloatField(default=-1)
    cached_longitude = models.FloatField(default=-1)


    # sean = models.ImageField()

    def add_rating(self,rating):
        numerator = (self.num_ratings*self.rating) + rating
        denominator = self.num_ratings + 1
        print("ans =",numerator/denominator)
        print("num =",self.num_ratings)
        self.rating = numerator/denominator
        self.num_ratings = denominator
        self.save()

    def get_condensed_address(self):
        return self.address.split("Charlottesville")[0]

    def print_details(self): # pragma no cover (used for debugging)
        print("debugging info:")
        print("-"*30)
        for i in self.__dict__:
            print(i," = ",self.__dict__[i])
        print("-"*30)

    def get_json(self):
        return dict_to_json(self.__dict__)

    def __str__(self):
        return str(self.name)

    def get_day(self):
        return self.submission_date.strftime("%m/%d/%Y")

    def add_image(self,path):
        image = Listing_Image.create(self,path)
        image.save()


    def get_coordinates(self):
        if(self.cached_latitude == -1 or self.cached_longitude == -1):
            print("geolocating",self.name + "...")
            geolocator = Nominatim()
            try:
                location = geolocator.geocode(self.address,timeout=10)
            except geopy.exc.GeocoderTimedOut:
                print("Geolocating %s (%s) timed out" % (self.name,self.address))
                return 0,0
            if(location == None):
                print("Geolocation failed")
                self.cached_latitude,self.cached_longitude = 0,0
                self.save()
                return 0,0
            self.cached_latitude,self.cached_longitude = location.latitude, location.longitude
            self.save()
        else:
            print("geolocation cached! (%s)" % self.name)

        return (self.cached_latitude,self.cached_longitude)

    @property
    def latitude(self):
        return self.get_coordinates()[0]

    @property
    def longitude(self):
        return self.get_coordinates()[1]


    @classmethod
    def get_sorted(cls,key):
        if type(key) != str:
            raise TypeError("Sorting key should be a string")

        if key not in cls.__dict__:
            raise KeyError("Key not found: " + key)

        out = cls.objects.all()
        out_sorted = sorted(out,key=lambda i: i.__dict__[key])
        return out_sorted

    @classmethod
    def get_in_price_range(cls,low,high):
        return cls.objects.filter(price__gte=low,price__lte=high)

class Listing_Image(models.Model):
    listing = models.ForeignKey(Listing, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to=("listing_pics/"))

    @classmethod
    def create(cls,listing,image):
        out = cls()
        out.listing = listing
        out.image = image
        return out

    def __str__(self):
        return str(self.image)


class Review(models.Model):
    listing = models.ForeignKey(Listing, related_name='reviews',on_delete=models.CASCADE)
    body = models.TextField(default="")
    user = models.ForeignKey(User, related_name='reviews',null=True,on_delete=models.SET_NULL)

    @classmethod
    def create(cls,listing,body,user):
        r = cls()
        r.listing = listing
        r.body = body
        r.user = user
        return r


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
