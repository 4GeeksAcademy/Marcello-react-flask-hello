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

    return jsonify(character), 200