'''
Created on Mar 13, 2016
@author: Tim
'''
'''
http://api.wunderground.com/api/APIKEY/features(/features/features...)/settings/q/query.format
'''

import urllib.request
import json

class API_Interface:
    api_key = "/a309444bd6a6e4db"   #Personal key
    base_url = "http://api.wunderground.com/api"
    request_string = "/q"
    end_string = ".json"
    DEFAULT_FEATURE = "/conditions/astronomy"
    DEFAULT_LOCATION = "/pws:KNJWESTW4" #Weather station next to HSS

    def __init__(self, location_string = "/pws:KNJWESTW4", feature_string = "/conditions/astronomy"):
        self.location_string = location_string
        self.feature_string = feature_string
    
    def get_complete_url(self):
        complete_url = self.base_url + self.api_key + self.feature_string + self.request_string + self.location_string + self.end_string
        return complete_url
    
    def update_data(self):
        raw_json = urllib.request.urlopen(self.get_complete_url()).read()
        # print(raw_json)
        raw_json = str(raw_json).replace(r"\n", "")
        raw_json = str(raw_json).replace(r"\t", "")
        # print(raw_json)
        raw_json = raw_json[2:-1]
        # print(raw_json)
        self.parsed_json = json.loads(raw_json)
    
    def get_parsed_data(self):
        return self.parsed_json


    
interface = API_Interface("/NJ/Plainsboro", "/conditions")
interface.update_data()
parsed_data = interface.get_parsed_data()

print(parsed_data['current_observation']['feelslike_string'])


