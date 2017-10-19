from flask import Blueprint, jsonify


users_blueprint = Blueprint('users', __name__)

# created new blueprint and bound the ping_pong function to it 
@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
