import os
from flask import Flask, jsonify
app = Flask(__name__)

# sets our config via the flask .from_object
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
