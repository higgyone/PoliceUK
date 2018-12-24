import json
import collections

class CrimeAtLoc(object):
    """description of class"""

    def __init__(self):
        self.category = None
        self.location_type = None
        self.location_subtype = None
        self.persistent_id = None
        self.month = None
        self.location_lat = None
        self.location_lng = None
        self.location_street_id = None
        self.location_street_name = None
        self.context = None
        self.id = None
        self.status_category = None
        self.status_date = None

    def string(self):
        return "Category: {}\n" \
        "Location type: {}".format(self.category, self.location_type)



    def __str__(self):
        return "Category: {}\n" \
        "Location type: {}\n" \
        "Location subtype: {}\n" \
        "Persistent Id: {}\n" \
        "ID: {}\n" \
        "Month: {}\n" \
        "Latitude: {}\n" \
        "Longitude: {}\n" \
        "Street ID: {}\n" \
        "Street Name: {}\n" \
        "Status category: {}\n" \
        "status date: {}" \
        .format(self.category, self.location_type, self.location_subtype, self.persistent_id,
                self.id, self.month, self.location_lat, self.location_lng, self.location_street_id,
                self.location_street_name, self.status_category, self.status_date)

    


    @staticmethod
    def ParseCrimeAtLoc(data):
        l = []
        
        for d in data:
            c = CrimeAtLoc()
            c.category = d["category"]
            c.location_type = d["location_type"]
            c.location_lat = d["location"]["latitude"]
            c.location_lng = d["location"]["longitude"]
            c.location_street_id = d["location"]["street"]["id"]
            c.location_street_name = d["location"]["street"]["name"]
            c.context = d["context"]
            if d["outcome_status"] is not None:
                c.status_category = d["outcome_status"]["category"]
                c.status_date = d["outcome_status"]["date"]
            c.id = d["id"]
            c.location_subtype = d["location_subtype"]
            c.month = d["month"]
            c.persistent_id = d["persistent_id"]

            l.append(c)

        return l
            
