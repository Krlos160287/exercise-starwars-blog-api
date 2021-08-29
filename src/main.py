"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, People, Planet, User, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods = ['GET'])
def getAll():
    peoples = People.get_All()
    return jsonify(peoples), 200

@app.route('/people/<int:id>', methods = ['GET'])
def getPeople(id):
    people = People.getPeople(id)
    return jsonify(people), 200

@app.route('/planets', methods = ['GET'])
def get_All():
    planets = Planet.get_All()
    return jsonify(planets),200

@app.route('/planets/<int:id>', methods = ['GET'])
def getPlanet(id):
    planet = Planet.getPlanet(id)
    return jsonify(planet), 200

@app.route('/users', methods =  ['GET'])
def getUsers():
    users = User.getUsers()
    return jsonify(users),200

@app.route('/favorite/<int:user_id>', methods = ['GET'])
def get_favorites_by_id(user_id):
    favorites = Favorite.get_favorites_by_id(user_id)
    return jsonify(favorites), 200

@app.route('/favorites', methods = ['POST'])
def createFavorite():
    body = request.get_json()
    if body is None:
        return{"error": "The body is empty or null"},400
    user = User.get_user(body['name'])
    user_id = user.id

    if "planet_id" in body:
        Favorite.createFavorite(user_id, None, planet_id)
        return {"message": "Planet added to Favorites"},200
    if "people_id" in body:
        Favorite.createFavorite(user_id, people_id, None)
        return {"message": "People added to Favorites"},200

@app.route('/favorites/<int:planet_id>', methods = ['DELETE'])
def deleteFavoritePlanet(planet_id):
    planet = deleteFavoritePlanet(planet_id)
    return jsonify(planet),200

@app.route('/favorites/<int:people_id>', methods = ['DELETE'])
def deleteFavoritePeople(people_id):
    user = User.get_user(body['name'])
    user_id = user.id
    people = deleteFavoritePeople(people_id)
    return jsonify(people),200
   

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
