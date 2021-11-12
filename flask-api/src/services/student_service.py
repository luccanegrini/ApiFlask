from src.models import db
from src.models.course import Course
from src.models.student import Student
from src.config.restplus import json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

from src.services.course_service import get as get_course


def create(data):
    try:
        name = data.get('name')
        if not name:
            json_abort(400, "Name is required")

        courseID = data.get('courseID')
        if not courseID:
            json_abort(400, "courseID is required")

        age = data.get('age')
        if not age:
            json_abort(400, "Age is required")

        cpf = data.get('cpf')
        if not cpf:
            json_abort(400, "cpf is required")

        course = get_course(courseID)

        created = datetime.datetime.now()

        student = Student(name=name, created=created, courseID=courseID, course=course, age=age, cpf=cpf)
        db.session.add(student)
        db.session.commit()

        return student

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        student = Student.query.join(Course, Course.courseID == Student.courseID)\
            .filter(Student.studentID == id).first()

        if not student:
            json_abort(400, "Student not found")
        else:
            return student

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def getAll():
    try:
        students = Student.query.all()
        return students

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def put(id, data):
    try:

        student = Student.query.filter_by(studentID=id).first()
        if not student:
            json_abort(400, "Student not found")
        else:
            name = data.get('name')
            if not name:
                json_abort(400, "Name is required")

            age = data.get('age')
            if not age:
                json_abort(400, "Age is required")

            cpf = data.get('cpf')
            if not cpf:
                json_abort(400, "cpf is required")

            student.name = name
            student.age = age
            student.cpf = cpf

            db.session.commit()

            return student

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:

        student = Student.query.filter_by(studentID=id).first()

        if not student:
            json_abort(400, "Student not found")
        else:
            db.session.delete(student)
            db.session.commit()

            return student

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)
