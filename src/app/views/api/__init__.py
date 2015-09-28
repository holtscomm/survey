"""
API endpoints
"""
import json
import webapp2


class JsonApiHandler(webapp2.RequestHandler):
    def return_json_response(self, data, status_code=200):
        return_dict = {
            'data': data,
            'status': status_code,
        }

        self.response.out.write(json.dumps(return_dict))
