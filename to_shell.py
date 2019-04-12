from users.models import UserProfile
from listings.models import Listing

l = Listing.objects.all()
standard = l[0]
sean = UserProfile.objects.all()[0]

# sean.favorites.remove(standard)
print(sean.favorites.all())

# standard.user_list.remove(sean)
print(standard.user_list.all())
print(standard.user_profile_list.all())
