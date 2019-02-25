from django.test import TestCase

from .models import Listing

def create_generic_listing():

	existing_ids = []
	for listing in Listing.objects.all():
		existing_ids.append(listing.id)


	unique_id = 0
	while unique_id in existing_ids:
		unique_id += 1

	out = Listing(unique_id,"name",5,"description","N",0,0,0,"123-456-7890","address","A")
	out.save()
	return out

# Note: The testing database is empty by default before each test
class ListingTest(TestCase):

	def setUp(self):
		pass

	def test_positional_arguments(self):
		l = Listing("id","name","rating","description","laundry_info","square_footage","price","bedroom_num","phone_num","address","ownership_info","submission_date")
		for item in l.__dict__:
			if item != "_state":
				self.assertEqual(item,l.__dict__[item],"Listing Constructor: Change detected in positional arguments (name or order). \nThrown for: Listing." + str(item))
		# l.print_details() # Uncomment to see how things fell into place

	def test_date_validation(self):
		l = Listing(submission_date="pizza")
		validated = True
		try:
			l.save()
			validated = False
		except:
			pass

		if(not validated):
			self.fail('Listing(submission_date = "pizza") should throw a ValidationError.')

	# Is this necessary?
	def test_create_generic_listing(self):
		a = create_generic_listing()
		b = create_generic_listing()
		c = create_generic_listing()
		self.assertEqual(3,len(Listing.objects.all()))

	def test_get_sorted(self):
		a = create_generic_listing()
		b = create_generic_listing()
		c = create_generic_listing()
