from flask import jsonify
from flask_restplus import Api

api = Api(version='1.0', title=' Post Service API',
          description='Api de gestão de posts')
    
def json_abort(status_code, message):
    data = {
        'error': {
            'code': status_code,
            'message': message
        }
    }
    response = jsonify(data)
    response.status_code = status_code
    api.abort(response)

def init_config(app):
    app.config['RESTPLUS_MASK_SWAGGER'] = False

 