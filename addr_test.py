import os

def read():
    os.system("pbpaste > paste.txt")
    y = open("paste.txt")
    out = y.read()
    y.close()
    os.remove("paste.txt")
    return out

address = read() # grabs from your clipboard
print("Testing address:",address)

from geopy import Nominatim

geolocator = Nominatim()
location = geolocator.geocode(address,timeout=10)
if location == None:
    print("failed")
else:
    print("success.")
    print(location.latitude,location.longitude)
