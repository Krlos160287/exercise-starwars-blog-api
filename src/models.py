from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            # do not serialize the password, its a security breach
        }
    def get_All():
        peoples = People.query.all()
        peoples = list(map(lambda people: people.serialize(), peoples))
        return peoples

    def getPeople(id):
        people = People.query.get(id)
        if people is None:
            return{"msg": "This character doesn't exist"}
        people = People.serialize(people)
        return people

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Planet %r>" % self.name
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population,
        }
    def get_All():
        planets = Planet.query.all()
        planets = list(map(lambda planet: planet.serialize(), planets))
        return planets
    
    def getPlanet(id):
        planet = Planet.query.get(id)
        if planet is None:
            print({"msg":"This planet doesn't exist "})
        planet = Planet.serialize(planet)
        return planet

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
    def getUsers():
        users = User.query.all()
        users = list(map(lambda user: user.serialize(), users))
        return users

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref = db.backref('my_favorite_list', lazy = 'dynamic'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    people = db.relationship('People', backref = db.backref('my_favorite_list', lazy = 'dynamic'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet', backref = db.backref('my_favorite_list', lazy = 'dynamic'))
    
    def serialize(self):
        return{
            "id": self.id,
            "user_add_favorite": self.user_id,
            "planet_date": self.planet_id
        }

    def get_favorites_by_id(user_id):
        favorites = Favorite.query.filter_by(user_id = user_id)
        favorites = list(map(lambda favorite: favorite.serialize(), favorites))
        return favorites
    
    def createFavorite(user_id, people_id, planet_id):
        favorite = Favorite(user_id = user_id, people_id = people_id, planet_id = planet_id)
        db.session.add(favorite)
        db.session.commit()

    def deleteFavoritePlanet(planet_id):
        planet = Planet.query.delete(planet_id)
        db.session.commit()