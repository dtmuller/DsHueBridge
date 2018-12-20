from datetime import datetime
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Description XML
@app.route("/description.xml")
def index():
    return config.DESCRIPTION_XML

# Read/write config
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

# Read full config
class FullConfig(Resource):
    def get(self, user):
        if user == config.USER:
            return config.HueConfig
        else:
           return [{"error":{"type":1,"address":"/","description":"unauthorized user"}}]

# Handle lights, groups, sensors
class Devices(Resource):
    def get(self, user, devices):
        if user == config.USER:
            if devices == "lights":
                return config.HueConfig["lights"]
            elif devices == "groups":
                return config.HueConfig["groups"]
            elif devices == "sensors":
                return config.HueConfig["sensors"]
            else:
                return [{"error":{"type":3,"address":f"/{devices}","description":f"resource, /{devices}, not available"}}]
        else:
           return [{"error":{"type":1,"address":f"/{devices}","description":"unauthorized user"}}]

# Discover light, groups, sensors
class NewDevices(Resource):
    def get(self, user, devices):
        if user == config.USER:
            return {"lastscan":"none"}
        else:
           return [{"error":{"type":1,"address":f"/{device}","description":"unauthorized user"}}]

# Create new user
class CreateUser(Resource):
    def post(self):
        return [{"success":{"username":config.USER}}]

api.add_resource(NewDevices, "/api/<string:user>/<string:devices>/new")
api.add_resource(Devices,    "/api/<string:user>/<string:devices>")
api.add_resource(Config,     "/api/<string:user>/config")
api.add_resource(FullConfig, "/api/<string:user>")
api.add_resource(CreateUser, "/api")

if __name__ == "__main__":
    import config
    app.run(host="0.0.0.0", port=80, debug=True)

