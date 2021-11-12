from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.course_serializer import course_request, course_result
from src.services.course_service import create, put, delete, get, getAll

ns = api.namespace('api/course', description='Course endpoints')


@ns.route('')
class CourseCollection(Resource):
    @api.expect(course_request)
    @api.marshal_with(course_result)
    def post(self):
        course = create(request.json)
        return course

    @api.marshal_with(course_result)
    def get(self):
        courses = getAll()
        return courses

@ns.route('/<int:id>')
class CourseIDCollection(Resource):
    @api.marshal_with(course_result)
    def get(self, id):
        course = get(id)
        return course

    @api.expect(course_request)
    @api.marshal_with(course_result)
    def put(self, id):
        course = put(id, request.json)
        return course

    @api.marshal_with(course_result)
    def delete(self, id):
        course = delete(id)
        return course
