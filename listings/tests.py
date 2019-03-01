from django.test import TestCase

from .models import Listing

def create_generic_listing(**kwargs):
	out = Listing(**kwargs)
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

	# Todo: add tests for sorting by other fields

	def test_get_in_price_range(self):
		a = create_generic_listing(name="a",price=1)
		b = create_generic_listing(name="b",price=2)
		c = create_generic_listing(name="c",price=3)
		d = create_generic_listing(name="d",price=4)
		e = create_generic_listing(name="e",price=5)
		f = create_generic_listing(name="f",price=6)
		g = create_generic_listing(name="g",price=7)
		h = create_generic_listing(name="h",price=8)
		self.assertEqual({c,d,e,f},set(Listing.get_in_price_range(3,6)))
