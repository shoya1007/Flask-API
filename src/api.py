from flask import Blueprint, request, jsonify
from models import db, City, CitySchema, Country
import requests

api = Blueprint('api', __name__, url_prefix='/flask')


@api.route('/', methods=['GET'])
def index():
    return jsonify({'test': 'Hello! This is City API'})


@api.route('/city', methods=['GET'])
def fetch_cities():
    # クエリパラメータを取得
    req = request.args
    # クエリパラメータがある場合
    if req:
        city_id = req.get('city_id')
        city = db.session.query(City).filter(City.id == city_id).one()
        if city:
            city_schema = CitySchema()
            return jsonify(city_schema.dump(city)), 200
        else:
            return jsonify({}), 404

    # クエリパラメータがない場合
    else:
        cities = db.session.query(City).all()
        if cities:
            city_schema = CitySchema(many=True)
            return jsonify(city_schema.dump(cities)), 200
        else:
            return jsonify({}), 404


@api.route('/cities/', methods=['GET'])
def fetch_cities_limit():

    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)
    cities = db.session.query(City).limit(limit).offset(offset).all()
    if cities:
        city_schema = CitySchema(many=True)
        return jsonify(city_schema.dump(cities)), 200
    else:
        return jsonify({}), 404


@api.route('/ctiyWithCountry/', methods=['GET'])
# Enum型でエラーが出るため現在使用不可
def fetch_cities_with_country():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)
    cities = db.session.query(City, Country).join(
        Country, City.country_code == Country.code).limit(limit).offset(offset).all()
    if cities:
        city_schema = CitySchema(many=True)
        return jsonify(city_schema.dump(cities)), 200
    else:
        return jsonify({}), 404


@api.route('/country/', methods=['GET'])
def fetch_countries_foreign_api():
    url = 'https://restcountries.eu/rest/v2/all'
    res = requests.get(url)
    return jsonify({'countries': res.json()}), 200


@api.errorhandler(400)
@api.errorhandler(401)
@api.errorhandler(403)
@api.errorhandler(404)
@api.errorhandler(500)
# エラーハンドリング
def error_handler(err):
    res = jsonify({
        'error': {
            'message': 'Error!Try again!'
        },
        'code': err.code
    })
    return res, err.code
