import os
from listings.models import *
# import datetime

def save_image_from(url,filename):
    path = "media/listing_pics/"
    command = "curl " + url + " > " + path + filename
    print(command)
    os.system(command)

def get_csv(filename):
    y = open("make_database.csv")
    lines = y.readlines()
    keys = list(map(str.strip,lines.pop(0).split(",")))
    while "" in keys:
        keys.remove("")
    out = [] # list of dicts
    for line in lines:
        d = {}
        lst = list(map(str.strip,line.split(",")))
        for i in range(len(lst)):
            item = lst[i]
            if i < len(keys):  # puts all extras in a list under that key
                key = keys[i]
                d[key] = item
            elif i == len(keys):
                key = keys[-1]
                d[key] = [d[key],item]
            else:
                key = keys[-1]
                d[key].append(item)
        out.append(d)
    return out

# def now(): # import datetime
#     return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

l = get_csv("make_database.csv")
# for i in l:
#     for j in i:
#         print(j,"->",i[j])
current_listings = Listing.objects.all()
for listing in l:

    name = listing["name"]
    query = current_listings.filter(name=name)
    listing["submission_date"] = "2019-04-01 00:00"
    if listing["description"] == "":
        listing["description"] = "Tucked away in northwestern London, a twenty minute walk from King's Cross Station, lies %s. Both Unplottable and hidden behind a Fidelius Charm, the house is invisible to all but a few. Though the neighbouring Muggles don't even know the building exists, it was for many years home to the Black family — one of the wizarding world's oldest pureblood families, and extremely proud to be so...It's ideal for Headquarters, of course. My father put every security measure known to wizardkind on it when he lived here. It's unplottable, so Muggles could never come and call — as if they'd ever have wanted to — and now Dumbledore's added his protection, you'd be hard put to find a safer house anywhere." % (name)

    l2 = {}
    for key in listing:
        if listing[key] != "":
            l2[key] = listing[key]
    listing = l2


    if len(query) != 0:
        for q in query:
            query.delete()
        print("Updating listing " + name + "...")
    else:
        print("Creating listing " + name + "...")

    pic_urls = listing.pop("pic_urls")
    listing = Listing(**listing)

    try:
        listing.save()
    except Exception as e:
        print("\n"+"-"*30,"\nError on ",name,"\n"+"-"*30+"\n")
        raise(e)

    counter = 1
    for url in pic_urls:
        extension = url[url.rfind("."):]
        filename = name + "_" + str(counter) + extension
        filename = filename.replace(" ","_")
        counter += 1
        save_image_from(url,filename)

        listing.add_image("listing_pics/" + filename)


    try:
        listing.save()
    except Exception as e:
        print("\n"+"-"*30,"\nError on ",name,"\n"+"-"*30+"\n")
        raise(e)



# make a listing
  # save images for that listing
