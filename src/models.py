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
        return "<Planet %r>" % self.nam
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population,
        }