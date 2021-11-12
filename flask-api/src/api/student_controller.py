from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.student_serializer import student_request, student_result
from src.services.student_service import create, put, delete, get, getAll

ns = api.namespace('api/student', description='Student endpoints')


@ns.route('')
class StudentCollection(Resource):
    @api.expect(student_request)
    @api.marshal_with(student_result)
    def post(self):
        student = create(request.json)
        return student

    @api.marshal_with(student_result)
    def get(self):
        students = getAll()
        return students

@ns.route('/<int:id>')
class StudentIDCollection(Resource):
    @api.marshal_with(student_result)
    def get(self, id):
        student = get(id)
        return student

    @api.expect(student_request)
    @api.marshal_with(student_result)
    def put(self, id):
        student = put(id, request.json)
        return student

    @api.marshal_with(student_result)
    def delete(self, id):
        student = delete(id)
        return student