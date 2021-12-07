from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class bdaywish(Resource):
    def post(self):
        data = request.get_json()
        display_name = data['data']

        bday_wish = "Happy Birthday, " + display_name + "!"
        json_str = '{"data": "' + bday_wish + '"}'

        return json_str

api.add_resource(bdaywish, '/bdaywish')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000)
