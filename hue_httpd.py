from datetime import datetime
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/description.xml")
def index():
    return config.DESCRIPTION_XML

class Config(Resource):
    def get(self, user):
        if user == config.USER:
            return config.HueConfig["config"]
        else:
            return config.HueBasic["config"]

    def put(self, user):
        if user == config.USER:
            #TODO verify and save data, echo back data
            return [{"success":{}}]
        else:
            return [{"error":{"type":1,"address":"/config","description":"unauthorized user"}}]

class Full(Resource):
    def get(self, user):
        if user == config.USER:
            return config.HueConfig
        else:
           return [{"error":{"type":1,"address":"/","description":"unauthorized user"}}]

class Lights(Resource):
    def get(self, user):
        if user == config.USER:
            return config.HueConfig["lights"]
        else:
           return [{"error":{"type":1,"address":"/lights","description":"unauthorized user"}}]

class Groups(Resource):
    def get(self, user):
        if user == config.USER:
            return config.HueConfig["groups"]
        else:
           return [{"error":{"type":1,"address":"/groups","description":"unauthorized user"}}]

class Sensors(Resource):
    def get(self, user):
        if user == config.USER:
            return config.HueConfig["sensors"]
        else:
           return [{"error":{"type":1,"address":"/sensors","description":"unauthorized user"}}]

class New(Resource):
    def get(self, user, device):
        if user == config.USER:
            return {"lastscan":"none"}
        else:
           return [{"error":{"type":1,"address":"/{}".format(device),"description":"unauthorized user"}}]

class User(Resource):
    def post(self):
        return [{"success":{"username":config.USER}}]

#TODO Must also work for api/config & api/a/b/config
api.add_resource(New, "/api/<string:user>/<string:device>/new")
api.add_resource(Sensors, "/api/<string:user>/sensors")
api.add_resource(Groups, "/api/<string:user>/groups")
api.add_resource(Lights, "/api/<string:user>/lights")
api.add_resource(Config, "/api/<string:user>/config")
api.add_resource(Full, "/api/<string:user>")
api.add_resource(User, "/api")

if __name__ == "__main__":
    import config
    app.run(host="0.0.0.0", port=80, debug=True)

