from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.apps import apps

# from listings.models import Listing
# import django.db.models
# from django.apps import apps
# MyModel1 = apps.get_model('listings', 'Listing')

# from django.contrib.auth.signals import user_logged_in

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprofile')
    # avatar = models.ImageField()
    dummyfield = models.IntegerField(default=5)
    favorites = models.ManyToManyField("listings.Listing",blank=True)

    def __str__(self):
        return "<UserProfile for " + self.user.username + ">"

    @classmethod
    def get_user(cls,username):
        all = cls.objects.all()
        for u in all:
            if u.user.username == username:
                return u

# @receiver(pre_delete)
# def delete_profile(sender, instance, **kwargs):
#     if sender == UserProfile:
#         instance.user.delete()
        # Listing = apps.get_model('listings', 'Listing')
        # for l in Listing.objects.all():
        #     if(instance in )

# def do_stuff(sender, user, request, **kwargs): #https://stackoverflow.com/questions/1990502/django-signal-when-user-logs-in
#     whatever...




# class LeasingAgent(UserProfile):

# class HousingAuthority(UserProfile):


#scary copy pasted code
#Create UserProfile upon new User signing in
# https://github.com/maxg203/Django-Tutorials/blob/master/accounts/models.py
def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if UserProfile.get_user(user.username) == None:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

# user_logged_in.connect(create_profile)
