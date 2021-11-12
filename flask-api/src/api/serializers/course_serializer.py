from flask_restplus import fields
from src.config.restplus import api


course_request = api.model('Course Request', {
    'name': fields.String(required=True, description='text course') ,
    'studyArea': fields.String(required=True, description='text course')
})

course_result = api.model('Course Result', {
    'courseID': fields.Integer(required=True, description='Course Id'),
    'name': fields.String(required=True, description='text course'),
    'studyArea': fields.String(required=True, description='text course')
})