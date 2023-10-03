from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

favorite_character=db.Table("favorite_character",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("character_id", db.Integer, db.ForeignKey("character.id"), primary_key=True)
)
favorite_episode=db.Table("favorite_episode",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("episode_id", db.Integer, db.ForeignKey("episode.id"), primary_key=True)
)
favorite_location=db.Table("favorite_location",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("location_id", db.Integer, db.ForeignKey("location.id"), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, )
    name = db.Column(db.String(80), unique=False, nullable=True )
    character = db.relationship("Character", secondary=favorite_character)
    episode = db.relationship("Episode", secondary=favorite_episode)
    location = db.relationship("Location", secondary=favorite_location)
    

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "favorite":self.favorite
            # do not serialize the password, its a security breach
        },

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, )
    gender = db.Column(db.String(80), unique=False, )
    status = db.Column(db.String(80), unique=False, )
    species = db.Column(db.String(80), unique=False, )
    origin = db.Column(db.String(80), unique=False, )
    location = db.Column(db.String(80), unique=False, )
    image = db.Column(db.String(150), unique=True, )
    episode = db.Column(db.String(80), unique=False, )    

    def __repr__(self):
        return f'<Character {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "gender": self.gender,
            "name": self.name,
            "status":self.status,
            "species":self.species,
            "origin":self.origin,
            "location":self.location,
            "image":self.image,
            "episode":self.episode
        },

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, )
    air_date = db.Column(db.String(80), unique=False, )
    episode = db.Column(db.String(80), unique=False, )
    character = db.Column(db.String(80), unique=False, )
    image = db.Column(db.String(150), unique=True, )    

    def __repr__(self):
        return f'<Episode {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "air.date":self.air.date,
            "episode":self.episode,
            "character":self.character,
            "image":self.image           
        },

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, )
    location_type = db.Column(db.String(80), unique=False, )
    dimension = db.Column(db.String(80), unique=False, )
    residents = db.Column(db.String(80), unique=False, )
    image = db.Column(db.String(150), unique=True, )    

    def __repr__(self):
        return f'<Location {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "location_type":self.location_type,
            "dimension":self.dimension,
            "residents":self.residents,
            "image":self.image
        }