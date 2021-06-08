from flask import Blueprint, request, jsonify
from models import City, CitySchema, db

api = Blueprint('api', __name__, url_prefix='/flask')


@api.route('/', methods=['GET'])
def index():
    return jsonify({'test': 'Hello! This is City API'})


@api.route('/city/', methods=['GET'])
def fetch_cities():
    cities = db.session.query(City).all()
    if cities:
        city_schema = CitySchema(many=True)
        return jsonify(city_schema.dump(cities)), 200
    else:
        return jsonify({}), 404


@api.route('/city/limit/', methods=['GET'])
def fetch_cities_limit():
    cities = db.session.query(City).limit(10).all()
    if cities:
        city_schema = CitySchema(many=True)
        return jsonify(city_schema.dump(cities)), 200
    else:
        return jsonify({}), 404
