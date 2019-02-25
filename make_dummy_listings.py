from listings.models import Listing

with open("dummy_listings.csv") as y:
    lines = y.readlines()

lines.pop(0)

for line in lines:
    line_list = line.strip().split(",")
    if len(line_list) > 0 and line_list[0] != '':
        l = Listing(*line_list)
        l.print_details()
        l.save()
