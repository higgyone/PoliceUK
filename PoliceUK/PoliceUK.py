import requests
import json
from CrimeAtLoc import CrimeAtLoc
import Area


def date_hook(r, *args, **kwargs):
    r.hook_called = True
    return r

def print_url(r, *args, **kwargs):
    print(r.url)

atLocUrlBase = "https://data.police.uk/api/crimes-at-location"


date = '2018-10'
payload = {'date' : date, 'lat' : Area.Latitude, 'lng' : Area.Longitude}

r = requests.get(atLocUrlBase, params=payload, hooks = {'response' : [print_url, date_hook]})

crimes = json.loads(r.text)

l = CrimeAtLoc.ParseCrimeAtLoc(crimes)

for i, val in enumerate(l):
    print(type(val))
    print(val)

#print(r.url)
#print(r.status_code)
#print(r.headers)
#print(r.content)
#print(r.json())
#print(r.hook_called)




