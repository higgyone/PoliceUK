import json
from CrimeAtLoc import CrimeAtLoc
import Area #use this to set your latitude and longitude
from DateIterator import DateIterator
from CrimeRequest import CrimeRequest

lCrimes = []

#def date_hook(r, *args, **kwargs):
#    r.hook_called = True
#    return r

atLocUrlBase = "https://data.police.uk/api/crimes-at-location"

cr = CrimeRequest(atLocUrlBase)

for dateStr in DateIterator():
    payload = {'date' : dateStr, 'lat' : Area.Latitude, 'lng' : Area.Longitude}

    cr.SetPayload(payload)
    #cr.SetHookCallback(print_url)

    r = cr.RunRequest()

    # check data available 
    if r.status_code == 500:
        print("500 error")
        continue

    if r.status_code == 404:
        print("404 error")
        continue

    crimes = json.loads(r.text)

    l = CrimeAtLoc.ParseCrimeAtLoc(crimes)

    print('*' * 12 + dateStr + '*' * 11)

    for i, val in enumerate(l):
        print(val)
        lCrimes.append(val)
        print('*' * 30)

    print('*' * 30)
