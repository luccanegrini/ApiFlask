from flask_restplus import fields
from src.api.serializers.student_serializer import student_result
from src.config.restplus import api


schoolTest_request = api.model('SchoolTest Request', {
    'title': fields.String(required=True, description='text schoolTest'),
    'concept': fields.String(required=True, description='text schoolTest'),
    'studentID': fields.Integer(required=True, description='schoolTest student ID '),
    'testGrade': fields.Integer(required=True, description='integer schoolTest')
})

schoolTest_result = api.model('SchoolTest Result', {
    'schoolTestID': fields.Integer(required=True, description='schoolTest Id'),
    'title': fields.String(required=True, description='text schoolTest'),
    'concept': fields.String(required=True, description='text schoolTest'),
    'student': fields.Nested(student_result, allow_null=False),
    'testGrade': fields.Integer(required=True, description='integer schoolTest'),
    'created': fields.String(required=True, description='date schoolTest created')
})
