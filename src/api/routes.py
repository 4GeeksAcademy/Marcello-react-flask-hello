"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Episode, Location
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

@api.route('/character', methods=['GET'])
def handle_Characters():
    character_list=Character.query.all()
    character_serialize=[character.serialize() for character in character_list]
    print(character_serialize)
    return jsonify(character_serialize), 200

@api.route('/character/<int:char_id>', methods=['GET'])
def handle_One_Characters(char_id):
    character=Character.query.filter_by(id=char_id).first()

    return jsonify(character.serialize()), 200

@api.route('/episode', methods=['GET'])
def handle_Episode():
    episode_list=Episode.query.all()
    episode_serialize=[episode.serialize() for episode in episode_list]
    print(episode_serialize)
    return jsonify(episode_serialize), 200

@api.route('/episode/<int:epis_id>', methods=['GET'])
def handle_One_Episode(epis_id):
    episode=Episode.query.filter_by(id=epis_id).first()

    return jsonify(episode.serialize()), 200

@api.route('/location', methods=['GET'])
def handle_Location():
    location_list=Location.query.all()
    location_serialize=[location.serialize() for location in location_list]
    print(location_serialize)
    return jsonify(location_serialize), 200

@api.route('/location/<int:loca_id>', methods=['GET'])
def handle_One_Location(loca_id):
    location=Location.query.filter_by(id=loca_id).first()

    return jsonify(location.serialize()), 200

@api.route('/users', methods=['GET'])
def handle_Users():
    users_list=User.query.all()
    users_serialize=[users.serialize() for users in users_list]
    print(users_serialize)
    return jsonify(users_serialize), 200

@api.route('/users/<int:user_id>', methods=['GET'])
def handle_One_Users(user_id):
    users=User.query.filter_by(id=user_id).first()

    return jsonify(users.serialize()), 200

@api.route('/users/favorites/<int:user_id>', methods=['GET'])
def get_user_favorites(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user_id is None:
        return jsonify({"error": "User ID is required"}), 400
    favorite_list=[]
    if user:
        favorite_characters = [character.serialize() for character in user.character]
        favorite_episodes = [episode.serialize() for episode in user.episode]
        favorite_locations = [location.serialize() for location in user.location]

        favorites = {
            "favorite_characters": favorite_characters,
            "favorite_episodes": favorite_episodes,
            "favorite_locations": favorite_locations
        }
        return jsonify(favorites), 200
    else:
        return jsonify({"error": "User not found"}), 404

@api.route('/favorite/character/<int:char_id>', methods=['POST'])
def add_favorite_character(char_id):
    user_id = request.json.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    favorite_character = Character.query.filter_by(id=char_id).first()
    
    if user and favorite_character:
        user.character.append(favorite_character)
        db.session.commit()
        return jsonify({"message": "Character added to user's favorites"}), 201
    else:
        return jsonify({"error": "User or character not found"}), 404

@api.route('/favorite/episode/<int:epis_id>', methods=['POST'])
def add_favorite_episode(epis_id):
    user_id = request.json.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    favorite_episode = Episode.query.filter_by(id=epis_id).first()
    
    if user and favorite_episode:
        user.episode.append(favorite_episode)
        db.session.commit()
        return jsonify({"message": "Episode added to user's favorites"}), 201
    else:
        return jsonify({"error": "User or episode not found"}), 404

@api.route('/favorite/location/<int:loca_id>', methods=['POST'])
def add_favorite_location(loca_id):
    user_id = request.json.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    favorite_location = Location.query.filter_by(id=loca_id).first()
    
    if user and favorite_location:
        user.location.append(favorite_location)
        db.session.commit()
        return jsonify({"message": "Location added to user's favorites"}), 201
    else:
        return jsonify({"error": "User or location not found"}), 404

@api.route('/favorite/character/<int:char_id>', methods=['DELETE'])
def delete_favorite_character(char_id):
    user_id = request.json.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    favorite_character = Character.query.filter_by(id=char_id).first()

    if user and favorite_character:
        user.character.remove(favorite_character)
        db.session.commit()
        return jsonify({"message": "Character removed from user's favorites"}), 200
    else:
        return jsonify({"error": "User or character not found"}), 404

@api.route('/favorite/episode/<int:epis_id>', methods=['DELETE'])
def delete_favorite_episode(epis_id):
    user_id = request.json.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    favorite_episode = Episode.query.filter_by(id=epis_id).first()

    if user and favorite_episode:
        user.episode.remove(favorite_episode)
        db.session.commit()
        return jsonify({"message": "Episode removed from user's favorites"}), 200
    else:
        return jsonify({"error": "User or episode not found"}), 404

@api.route('/favorite/location/<int:loca_id>', methods=['DELETE'])
def delete_favorite_location(loca_id):
    user_id = request.json.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    favorite_location = Location.query.filter_by(id=loca_id).first()

    if user and favorite_location:
        user.location.remove(favorite_location)
        db.session.commit()
        return jsonify({"message": "Location removed from user's favorites"}), 200
    else:
        return jsonify({"error": "User or location not found"}), 404


