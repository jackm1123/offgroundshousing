from django.test import TestCase

from .models import Listing

class ListingTest(TestCase):

	def setUp(self):
		pass

	def test_positional_arguments(self):
		l = Listing("id","name","rating","description","submission_date","laundry_info","square_footage","price","bedroom_num","phone_num","address","ownership_info")
		for item in l.__dict__:
			if item != "_state":
				self.assertEqual(item,l.__dict__[item],"Listing Constructor: Change detected in positional arguments (name or order). \nThrown for: Listing." + str(item))
		# l.print_details() # Uncomment to see how things fell into place
