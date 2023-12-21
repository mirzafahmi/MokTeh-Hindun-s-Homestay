from flask import Blueprint, current_app, jsonify
from api.gmap_api import make_api_call

api_views = Blueprint('api', __name__)

@api_views.route('/gmap', methods=['GET'])
def map_api_data():
    api_key = current_app.config['GMAP_API_KEY']
    long= 40.758896
    lat= -73.985130
    data = make_api_call(api_key, long, lat)
    if data is not None:
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch data from the API'}), 500
