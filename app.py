'''
Flask App
'''
from flask import Flask
from flask_restful import Api  # pragma: no cover
from handlers.routes import configure_routes
from handlers.api import sampleAPI  # pragma: no cover

app = Flask(__name__)
api = Api(app)

api.add_resource(sampleAPI,'/api/test')
configure_routes(app)

if __name__ == '__main__':    #pylint disable=trailing-whitespace
    #app.run(debug=True)
    app.run(host="0.0.0.0", port="3000")





