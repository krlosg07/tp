from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Temp(Resource):
    def get(self):
        return {'temp': '25'}

class Hello(Resource):
     def get(self):
        return {'hello': 'Alors le r\'eseau c''est bien?'}

api.add_resource(Hello, '/')
api.add_resource(Temp, '/temperature')

if __name__ == '__main__':
    app.run(debug=True)
