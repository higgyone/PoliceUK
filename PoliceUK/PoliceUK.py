import requests
import json
from CrimeAtLoc import CrimeAtLoc
import Area #use this to set your latitude and longitude
from DateIterator import DateIterator


def date_hook(r, *args, **kwargs):
    r.hook_called = True
    return r

def print_url(r, *args, **kwargs):
    print(r.url)

atLocUrlBase = "https://data.police.uk/api/crimes-at-location"

for dateStr in DateIterator():
    print(dateStr)
    payload = {'date' : dateStr, 'lat' : Area.Latitude, 'lng' : Area.Longitude}

    r = requests.get(atLocUrlBase, params=payload, hooks = {'response' : [print_url, date_hook]})

    crimes = json.loads(r.text)

    l = CrimeAtLoc.ParseCrimeAtLoc(crimes)

    for i, val in enumerate(l):
        print(val)

#print(r.url)
#print(r.status_code)
#print(r.headers)
#print(r.content)
#print(r.json())
#print(r.hook_called)




