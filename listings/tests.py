from django.test import TestCase

from .models import Listing

def create_generic_listing(**kwargs):

	existing_ids = []
	for listing in Listing.objects.all():
		existing_ids.append(listing.id)

	unique_id = 0
	while unique_id in existing_ids:
		unique_id += 1

	out = Listing(unique_id)

	for key in kwargs:
		if key not in out.__dict__:
			raise KeyError("Invalid key: " + str(key))
		out.__dict__[key] = kwargs[key]

	out.save()

	return out

# Note: The testing database is empty by default before each test
class ListingTest(TestCase):

	def setUp(self):
		pass

	def test_positional_arguments(self):
		l = Listing("id","name","rating","description","laundry_info","parking_info","square_footage","price","bedroom_num","phone_num","address","ownership_info","submission_date")
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

	# Are these 3 tests necessary? Not testing Listing...
	def test_create_generic_listing(self):
		a = create_generic_listing()
		b = create_generic_listing()
		c = create_generic_listing()
		self.assertEqual(3,len(Listing.objects.all()))

	def test_create_generic_listing_kwargs(self):
		a = create_generic_listing(price=20)
		self.assertEqual(20,a.price)

	def test_create_generic_listing_invalid_kwargs(self):
		ok = False
		try:
			create_generic_listing(invalid="invalid")
		except KeyError:
			ok = True

		self.assertTrue(ok)

	def test_get_sorted_by_id(self):
		a = create_generic_listing(name="a",id=3)
		b = create_generic_listing(name="b",id=2)
		c = create_generic_listing(name="c",id=1)
		d = create_generic_listing(name="d",id=0)

		self.assertEqual([d,c,b,a],Listing.get_sorted("id"))

	def test_get_sorted_by_price(self):
		a = create_generic_listing(name="a",id=0,price=1)
		b = create_generic_listing(name="b",id=1,price=3)
		c = create_generic_listing(name="c",id=2,price=0)
		d = create_generic_listing(name="d",id=3,price=2)

		self.assertEqual([c,a,d,b],Listing.get_sorted("price"))
