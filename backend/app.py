from flask import Flask, jsonify, request
from flask_cors import CORS
import powerliftingLogic
import database.populatePowerliftingTable as powerliftingDB

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

    data = powerliftingLogic.analyze_powerlifting(lift_data)

    response = {
        'status': 'Success',
        'data': data
    }

    return jsonify(response)

# @app.route('/init-pl', methods=['POST'])
# def init_pl():
#     response = powerliftingDB.init_pl()
#
#     return jsonify(response)

def create_app(env):
    app = Flask(__name__)
    app.config['env'] = env
    print('Passed item: ', app.config['env'])

    # Populate powerlifting database prior to starting app if running on prod
    if(env == 'prod'):
        powerliftingDB.init_pl()

    return app

if __name__ == '__main__':
    # Start app
    app.run()