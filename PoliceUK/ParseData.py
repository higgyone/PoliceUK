from CrimeAtLoc import CrimeAtLoc

class Parser(object):
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
            c.status_category = d["outcome_status"]["category"]
            c.status_date = d["outcome_status"]["date"]
            c.id = d["id"]
            c.location_subtype = d["location_subtype"]
            c.month = d["month"]
            c.persistent_id = d["persistent_id"]

            l.append(c)

        return l



