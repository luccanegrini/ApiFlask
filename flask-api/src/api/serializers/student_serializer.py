from flask_restplus import fields
from src.api.serializers.course_serializer import course_result
from src.config.restplus import api

student_request = api.model('Student Request', {
    'name': fields.String(required=True, description='text student'),
    'age': fields.Integer(required=True, description='text student'),
    'cpf': fields.String(required=True, description='text student'),
    'courseID': fields.Integer(required=True, description='student course ID ')
})

student_result = api.model('Student Result', {
    'studentID': fields.Integer(required=True, description='student Id'),
    'name': fields.String(required=True, description='text student'),
    'age': fields.String(required=True, description='integer student'),
    'cpf': fields.String(required=True, description='text student'),
    'course': fields.Nested(course_result, allow_null=False),
    'created': fields.String(required=True, description='date student created')
})
