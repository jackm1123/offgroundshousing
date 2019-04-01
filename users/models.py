from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import listings.models
# from django.apps import apps
# MyModel1 = apps.get_model('listings', 'Listing')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField()
    dummyfield = models.IntegerField(default=5)
    favorites = models.ManyToManyField(listings.models.Listing)


# class LeasingAgent(UserProfile):

# class HousingAuthority(UserProfile):


#scary copy pasted code
#Create UserProfile upon new User signing in
# https://github.com/maxg203/Django-Tutorials/blob/master/accounts/models.py
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
    