META_TESTING = False
SYSTEM_TESTING = False

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Listing
import os,subprocess,sys

from django.test.utils import override_settings
from django.conf import settings

def create_generic_listing(**kwargs):
    out = Listing(**kwargs)
    out.save()
    return out

def get_command_output(command):
    command_lst = command.split()
    return subprocess.check_output(command_lst)

def debug_write(message):
    y = open("debug_output.txt","a")
    y.write("\n----------\n")
    y.write(message)
    y.close()

def exclude_from_metatest():
    return os.path.isfile("no_meta_test")

on_travis = 'TRAVIS' in os.environ

def ping_url(url):
    client = Client()
    response = client.get(url)
    stat = response.status_code
    return stat

# Note: The testing database is empty by default before each test
class ListingTest(TestCase):

    def setUp(self):
        pass

    # Super-hacky way of programatically testing our coverage levels
    # TODO: Make this not run all the tests twice...
    def test_meta(self):
        if not META_TESTING:
            return

        if(exclude_from_metatest()):
            return

        if os.system("coverage > no_meta_test") != 0:
            os.system("pip install coverage")
            os.system("pip3 install coverage")

        os.system("coverage run manage.py test >/dev/null 2>&1")
        os.remove("no_meta_test")
        coverage_info = get_command_output("coverage report").decode().split("\n")[2:-3]
        get_command_output("coverage html")

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
            error_message += "\n\n*******************\n\n"
            error_message = get_command_output("coverage report").decode() + error_message
            # if(coverage != "100%"):
            #     os.system("open htmlcov/index.html")
            self.assertEqual("100%",coverage,error_message)

    # def test_positional_arguments(self):
    #     l = Listing("id","name","rating","description","laundry_info","parking_info","square_footage","price","bedroom_num","phone_num","address","ownership_info","submission_date")
    #     for item in l.__dict__:
    #         if item != "_state":
    #             self.assertEqual(item,l.__dict__[item],"Listing Constructor: Change detected in positional arguments (name or order). \nThrown for: Listing." + str(item))
    #     # l.print_details() # Uncomment to see how things fell into place

    def test_str(self):
        a = create_generic_listing(name="test123")
        self.assertEqual("test123",str(a))

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

    def test_get_json(self):
        a = create_generic_listing()
        actual_output = a.get_json()

        for key,val in a.__dict__.items():
            key_quotes = '"%s"' %str(key)
            if type(val) != int:
                val_quotes = '"%s"' %str(val)
            else:
                val_quotes = '%s' %str(val)
            combined = key_quotes + ":" + val_quotes
            if combined not in actual_output:
                print(combined)
                print("-----")
                print(actual_output)
            self.assertTrue(combined in actual_output)

    def test_empty_url(self):
        self.assertEqual(200,ping_url("/"))

    def test_admin_url(self):
        self.assertEqual(302,ping_url("/admin/"))

    def test_listings_url(self):
        self.assertEqual(200,ping_url("/listings/"))

    def test_all_listings_pages(self):
        a = create_generic_listing(name="a",id=3)
        b = create_generic_listing(name="b",id=2)
        c = create_generic_listing(name="c",id=1)
        d = create_generic_listing(name="d",id=0)

        objs = Listing.objects.all()
        for o in objs:
            self.assertEqual(301,ping_url("/listings/" + str(o.id)))

    # def test_login_url(self):
    #     self.assertEqual(200,ping_url("/login/"))

    def test_logout_url(self):
        self.assertEqual(302,ping_url("/logout/"))

    def test_auth_url(self):
        self.assertEqual(302,ping_url("/auth/login/google-oauth2/"))

    def test_faulty_address_coordinates(self):
        a = create_generic_listing(name="Test property A",address="asdmnaskb",id=3)
        a.get_coordinates()

    def test_add_rating(self):
        a = create_generic_listing(rating=3.0, num_ratings= 9)
        rating = 5
        a.add_rating(rating)
        self.assertEqual(3.2,a.rating)
        self.assertEqual(10,a.num_ratings)

    def test_add_image(self):
        a = create_generic_listing()
        a.add_image("test.jpg")


################################################################################
""" System Tests """
################################################################################
def make_some_listings():
    a = create_generic_listing(name="Test property A",address="853 W Main St., Charlottesville, VA 22903",id=3)
    b = create_generic_listing(name="Test property B",address="301 15th St NW, Charlottesville, VA",id=2)
    c = create_generic_listing(name="Test property C",address="102 14th St NW, Charlottesville, VA",id=1)
    d = create_generic_listing(name="Test property D",address="101 14th St NW, Charlottesville, VA",id=0)
    return a,b,c,d

if SYSTEM_TESTING and not exclude_from_metatest():
    # https://lincolnloop.com/blog/introduction-django-selenium-testing/
    from selenium import webdriver
    from django.test import LiveServerTestCase
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    @override_settings(DEBUG=True)


    class SeleniumTest(LiveServerTestCase):

        # print(os.listdir())


        # def __init__(self, *args, **kwargs):
        #     super(LiveServerTestCase, self).__init__(*args, **kwargs)
        #     for i in self.__dict__:
        #         print(i)
        #     if self.settings.DEBUG == False:
        #         self.settings.DEBUG = True

        def setUp(self):
            # cap["marionette"] = False

            try:
                self.browser = webdriver.Firefox(executable_path="geckodriver")
                # self.browser = webdriver.Firefox()
            except Exception as e:
                print(e)
                print(open("geckodriver.log").read())
                raise e
            super(SeleniumTest, self).setUp()

        def tearDown(self):
            self.browser.close()
            self.browser.quit()

        def load(self,url):
            self.browser.get(self.live_server_url+url)

        # https://selenium-python.readthedocs.io/locating-elements.html
        def get_by_tag(self,id):
            return self.browser.find_elements_by_tag_name(id)

        def get_by_class(self,cls):
            return self.browser.find_elements_by_class_name(cls)

        def get_by_id(self,id):
            return self.browser.find_element_by_id(id)

        def get(self,css):
            return self.browser.find_elements_by_css_selector(css)

        def do_search_box(self,text):
            self.load("")
            search_box = self.get(".form-control")[0]
            search_box.click()
            search_box.send_keys(text)
            self.get(".btn-outline-success")[0].click()

        def check_for_listings(self,listings):
            l_s = self.get(".listing .name a")
            for l in l_s:
                self.assertTrue(l.text in listings)

        def load_filter_view(self):
            self.load("/listings/")
            self.get_by_id("filter").click()

        def enter_in_filter_form(self,id,text):
            self.load_filter_view()
            box = self.get_by_id(id)
            box.send_keys(text)
            self.get_by_id("apply_filters").click()




        ###############################################
        def test_selenium(self):
            self.load("")
            self.assertTrue(len(self.get_by_tag("h1")[0].text) > 0)

        def test_some_listings(self):
            a,b,c,d = make_some_listings()
            self.load("/listings/")
            divs = self.browser.find_elements_by_class_name("listing")
            self.assertEqual(4,len(divs))


        def test_rating(self):
            a = create_generic_listing(name="Test property A",address="301 15th St NW, Charlottesville, VA",rating=4,id=1)
            self.load("/listings/1/")
            for rating_pic in self.get(".rating img"):
                num = rating_pic.get_attribute("num")
                visible = rating_pic.is_displayed()
                if num == "4":
                    self.assertTrue(visible)
                else:
                    self.assertFalse(visible)


        def test_search_number(self):
            create_generic_listing(name="substring A",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="substring sa B",address="302 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="asd sdsubstringasd C",address="302 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="asdjklsubstringaslkjsd D",address="302 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="substring E",address="302 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="SUBSTRING F",address="302 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="__sUbStRiNg__ G",address="302 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="no substrinmatch",address="302 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="substrinngno s ubstring substrinmatch",address="302 15th St NW, Charlottesville, VA",rating=4)

            self.load("/search/?query=substring")
            listings = self.get(".listing")
            self.assertEqual(7,len(listings))



        def test_search_content(self):
            create_generic_listing(name="substring A",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="substring B",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="no match",address="301 15th St NW, Charlottesville, VA",rating=4)

            self.load("/search/?query=substring")
            listings = self.get(".listing .name a")
            for l in listings:
                self.assertTrue(l.text in ("substring A","substring B"))


        def test_search_stripped(self):
            create_generic_listing(name="substring A",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="substring B",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="no match",address="301 15th St NW, Charlottesville, VA",rating=4)

            self.load("/search/?query=%20%20substring%20%20")
            listings = self.get(".listing .name a")
            for l in listings:
                self.assertTrue(l.text in ("substring A","substring B"))


        def test_search_box(self):
            create_generic_listing(name="substring A",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="substring B",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="no match",address="301 15th St NW, Charlottesville, VA",rating=4)

            self.do_search_box("substr")

            listings = self.get(".listing .name a")
            for l in listings:
                self.assertTrue(l.text in ("substring A","substring B"))

        def test_search_and_click(self):
            create_generic_listing(name="substring A",address="301 15th St NW, Charlottesville, VA",rating=4)

            self.do_search_box("substr")
            self.get(".name a")[0].click()


        # def test_map_node_number(self):
        #     create_generic_listing(name="substring A",address="301 15th St NW, Charlottesville, VA",rating=4)
        #     create_generic_listing(name="substring B",address="301 15th St NW, Charlottesville, VA",rating=4)
        #     create_generic_listing(name="substring C",address="301 15th St NW, Charlottesville, VA",rating=4)
        #     create_generic_listing(name="substring D",address="301 15th St NW, Charlottesville, VA",rating=4)
        #     create_generic_listing(name="substring E",address="301 15th St NW, Charlottesville, VA",rating=4)
        #
        #     self.do_search_box("substr")
        #     all = self.get("area")
        #     self.assertEqual(5,len(all))



        def test_search_box_stripped(self):
            create_generic_listing(name="substring A",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="substring B",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="no match",address="301 15th St NW, Charlottesville, VA",rating=4)

            self.do_search_box("  substr  ")

            listings = self.get(".listing .name a")
            for l in listings:
                self.assertTrue(l.text in ("substring A","substring B"))


        def test_filter_by_name(self):
            create_generic_listing(name="substring A",address="301 15th St NW, Charlottesville, VA",rating=4)
            create_generic_listing(name="substring B",address="301 15th St NW, Charlottesville, VA",rating=4)
            self.enter_in_filter_form("name","substring A")
            self.check_for_listings(["substring A"])



        def test_filter_by_price_low(self):
            create_generic_listing(name="A",address="301 15th St NW, Charlottesville, VA",rating=4,price=200)
            create_generic_listing(name="B",address="301 15th St NW, Charlottesville, VA",rating=4,price=400)
            create_generic_listing(name="C",address="301 15th St NW, Charlottesville, VA",rating=4,price=600)
            create_generic_listing(name="D",address="301 15th St NW, Charlottesville, VA",rating=4,price=800)
            self.enter_in_filter_form("price_low","500")
            self.check_for_listings(["C","D"])

        def test_filter_by_price_high(self):
            create_generic_listing(name="A",address="301 15th St NW, Charlottesville, VA",rating=4,price=200)
            create_generic_listing(name="B",address="301 15th St NW, Charlottesville, VA",rating=4,price=400)
            create_generic_listing(name="C",address="301 15th St NW, Charlottesville, VA",rating=4,price=600)
            create_generic_listing(name="D",address="301 15th St NW, Charlottesville, VA",rating=4,price=800)
            self.enter_in_filter_form("price_high","500")
            self.check_for_listings(["A","B"])



        def test_filter_by_rating_low(self):
            create_generic_listing(name="A",address="301 15th St NW, Charlottesville, VA",rating=0,price=200)
            create_generic_listing(name="B",address="301 15th St NW, Charlottesville, VA",rating=1,price=400)
            create_generic_listing(name="C",address="301 15th St NW, Charlottesville, VA",rating=2,price=600)
            create_generic_listing(name="D",address="301 15th St NW, Charlottesville, VA",rating=3,price=800)
            create_generic_listing(name="E",address="301 15th St NW, Charlottesville, VA",rating=4,price=800)
            create_generic_listing(name="F",address="301 15th St NW, Charlottesville, VA",rating=5,price=800)
            self.enter_in_filter_form("rating_low","3")
            self.check_for_listings(["D","E","F"])

        def test_filter_by_rating_high(self):
            create_generic_listing(name="A",address="301 15th St NW, Charlottesville, VA",rating=0,price=200)
            create_generic_listing(name="B",address="301 15th St NW, Charlottesville, VA",rating=1,price=400)
            create_generic_listing(name="C",address="301 15th St NW, Charlottesville, VA",rating=2,price=600)
            create_generic_listing(name="D",address="301 15th St NW, Charlottesville, VA",rating=3,price=800)
            create_generic_listing(name="E",address="301 15th St NW, Charlottesville, VA",rating=4,price=800)
            create_generic_listing(name="F",address="301 15th St NW, Charlottesville, VA",rating=5,price=800)
            self.enter_in_filter_form("rating_high","3")
            self.check_for_listings(["A","B","C","D"])
