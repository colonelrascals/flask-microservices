from flask import Flask, jsonify
app = Flask(__name__)

# sets our config via the flask .from_object
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
