from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.schoolTest_serializer import schoolTest_request, schoolTest_result
from src.services.schoolTest_service import create, put, delete, get, getAll

ns = api.namespace('api/schooltest', description='School Test endpoints')


@ns.route('')
class SchoolTestCollection(Resource):
    @api.expect(schoolTest_request)
    @api.marshal_with(schoolTest_result)
    def post(self):
        schoolTest = create(request.json)
        return schoolTest

    @api.marshal_with(schoolTest_result)
    def get(self):
        tests = getAll()
        return tests

@ns.route('/<int:id>')
class SchoolTestIDCollection(Resource):
    @api.marshal_with(schoolTest_result)
    def get(self, id):
        schoolTest = get(id)
        return schoolTest

    @api.expect(schoolTest_request)
    @api.marshal_with(schoolTest_result)
    def put(self, id):
        schoolTest = put(id, request.json)
        return schoolTest

    @api.marshal_with(schoolTest_result)
    def delete(self, id):
        schoolTest = delete(id)
        return schoolTest