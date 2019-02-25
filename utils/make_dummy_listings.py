"""
This file will not run alone.
It must be run in the main directory by the following command:
    python3 manage.py shell < utils/make_dummy_listings.py
"""

from listings.models import Listing

with open("utils/dummy_listings.csv") as y:
    lines = y.readlines()

lines.pop(0)

for line in lines:
    line_list = line.strip().split(",")
    if len(line_list) > 0 and line_list[0] != '':
        l = Listing(*line_list)
        l.print_details()
        l.save()
