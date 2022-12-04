from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/analyze-lifts', methods=['POST'])
def analyze_lifts():
    lift_data = request.get_json()

    squat = lift_data.get('squat')
    bench = lift_data.get('bench')
    deadlift = lift_data.get('deadlift')
    units = lift_data.get('units')

    response = {
        'status': 'Success',
        'squat': squat,
        'bench': bench,
        'deadlift': deadlift,
        'units': units
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run()