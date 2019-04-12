from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.

counter = 1

def make_generic_user_profile(username):
    global counter
    a = User()
    a.username = username
    a.save()

    b = UserProfile()
    b.user = a

    b.save()
    return b

class ListingTest(TestCase):

    def setUp(self):
        pass

    def test_user_str(self):
        b = make_generic_user_profile("sgatewood")
        self.assertEqual("<UserProfile for sgatewood>",str(b))

    def test_get_user(self):
        a = make_generic_user_profile("user_a")
        b = make_generic_user_profile("user_b")
        c = make_generic_user_profile("user_c")

        self.assertEqual(a.user,UserProfile.get_user("user_a").user)
