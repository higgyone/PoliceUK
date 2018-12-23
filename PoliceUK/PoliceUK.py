import requests
import json
from CrimeAtLoc import CrimeAtLoc
from ParseData import Parser


def date_hook(r, *args, **kwargs):
    r.hook_called = True
    return r

def print_url(r, *args, **kwargs):
    print(r.url)

atLocUrlBase = "https://data.police.uk/api/crimes-at-location"
seymoreRoadLat = '53.358019'
seymoreRoadLng = '-1.309736'
date = '2018-10'
payloadSeymoreRd = {'date' : date, 'lat' : seymoreRoadLat, 'lng' : seymoreRoadLng}

r = requests.get(atLocUrlBase, params=payloadSeymoreRd, hooks = {'response' : [print_url, date_hook]})

crimes = json.loads(r.text)
#print(type(crimes))
#print(crimes[:10])

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


#r = requests.get('https://api.github.com/events')
#r.text
#jar = r.cookies
#print(jar)

