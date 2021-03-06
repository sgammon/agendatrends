from agendatrends.handlers import WebHandler
from sunlightapi import sunlight, SunlightApiError

import simplejson as json
import random


sunlight.apikey = 'e4d34e8391c44b7682915ababb408c65';


import logging

class ApiTopicHandler(WebHandler):

	def get(self, filters):
		import os
		logging.info(os.path.dirname(__file__))
		return open(os.path.dirname(__file__) + "/../../static/topics" + Topic.filterWith(TopicFilters(filters))).readlines()


class ApiLegislatorHandler(WebHandler):

    def get(self):
        response = sunlight.legislators.allForLatLong(self.request.args.get('latitude'), 
                                                 self.request.args.get('longitude'))

        params = {
            'latitude': self.request.args.get('latitude'),
            'longitude': self.request.args.get('longitude')
        }

        return json.dumps(sunlight._apicall('legislators.allForLatLong', params))


class ApiRepMentionsHandler(WebHandler):

    def get(self):
        reps = self.request.args.get("reps").split(',')
        
        
        return json.dumps( { "rep_mentions": map(self.convert_mentions, reps) })

    def convert_mentions(self, rep):
        return { "fec_id": rep,
                 "mentions": int(random.gauss(10.0, 3.0))
        }




