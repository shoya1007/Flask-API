from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__, url_prefix='/flask')


@api.route('/', methods=['GET'])
def index():
    return jsonify({'test': 'Hello! This is City API'})
