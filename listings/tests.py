from django.test import TestCase

from .models import Listing
import os,subprocess

def create_generic_listing(**kwargs):
    out = Listing(**kwargs)
    out.save()
    return out

def get_command_output(command):
    command_lst = command.split()
    return subprocess.check_output(command_lst)

# Note: The testing database is empty by default before each test
class ListingTest(TestCase): # pragma no cover

    def setUp(self):
        pass

    # Super-hacky way of programatically testing our coverage levels
    def test_meta(self):

        if subprocess.call("coverage") != 0:
            os.system("pip install coverage")
            os.system("pip3 install coverage")

        if(os.path.isfile("no_meta_test")):
            return

        y = open("no_meta_test","w")
        y.close()
        os.system("coverage run manage.py test")
        os.remove("no_meta_test")
        coverage_info = get_command_output("coverage report").decode().split("\n")[2:-3]
        os.system("coverage html")

        coverage_dict = {}
        for line in coverage_info:
            line_split = line.strip().split()
            file = line_split[0]
            coverage = line_split[3]
            coverage_dict[file] = coverage

        for file in coverage_dict:
            coverage = coverage_dict[file]
            error_message = "\n*******************\n\n"
            error_message += """  |||
  |||       _T_
  |||   .-.[:|:].-.
  ===_ /\|  "'"  |/
   M]_|\/ \--|-|''''|
   T  `'  '=[:]| M  |
          /""\""|  T |
         /""\""\"`.__.'
        []"/""\"\"[]
        | \     / |
        | |     | |
      <\\\)     (///>"""
            error_message += "\nOh no! You have been attacked by a wild META-TEST! \n\nCoverage in file '%s' is %s. You can get it to 100%%!" %(file,coverage)
            error_message += "\n\nRun one of these commands to check your test coverage:"
            error_message += "\n\t 1) open htmlcov/index.html"
            error_message += "\n\t 2) ./check-coverage.sh"

            error_message += "\n\nOptions to increase your coverage:"
            error_message += "\n\t1) Add tests that reach the uncovered lines"
            error_message += "\n\t2) Use '#pragma no cover' decorator if you really don't think a test is necessary"
            error_message += "\n\n*******************\n"
            # if(coverage != "100%"):
            #     os.system("open htmlcov/index.html")
            self.assertEqual("100%",coverage,error_message)





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

    def test_get_sorted_invalid_key_type(self):
        a = create_generic_listing(name="a",id=0,price=1)
        b = create_generic_listing(name="b",id=1,price=3)

        self.assertRaises(TypeError,Listing.get_sorted,key=0)

    def test_get_sorted_invalid_key_name(self):
        a = create_generic_listing(name="a",id=0,price=1)
        b = create_generic_listing(name="b",id=1,price=3)

        self.assertRaises(KeyError,Listing.get_sorted,key="dsghjdvgjsgjshvs")

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
