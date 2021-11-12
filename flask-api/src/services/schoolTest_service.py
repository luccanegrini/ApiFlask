from src.models import db
from src.models.schoolTest import SchoolTest
from src.config.restplus import json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

from src.models.student import Student
from src.services.student_service import get as get_student


def create(data):
    try:
        title = data.get('title')
        if not title:
            json_abort(400, "title is required")

        testGrade = data.get('testGrade')
        if not testGrade:
            json_abort(400, "testGrade is required")

        concept = data.get('concept')
        if not concept:
            json_abort(400, "concept is required")

        studentID = data.get('studentID')
        if not studentID:
            json_abort(400, "studentID is required")

        student = get_student(studentID)

        created = datetime.datetime.now()

        schoolTest = SchoolTest(title=title, created=created, studentID=studentID, student=student, testGrade=testGrade,
                                concept=concept)
        db.session.add(schoolTest)
        db.session.commit()

        return schoolTest

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        schoolTest = SchoolTest.query.join(Student, Student.studentID == SchoolTest.studentID) \
            .filter(SchoolTest.schoolTestID == id).first()

        if not schoolTest:
            json_abort(400, "School Test not found")
        else:
            return schoolTest

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def getAll():
    try:
        tests = SchoolTest.query.all()
        return tests

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def put(id, data):
    try:
        schoolTest = SchoolTest.query.filter_by(schoolTestID=id).first()

        if not schoolTest:
            json_abort(400, "School Test not found")
        else:

            title = data.get('title')
            if not title:
                json_abort(400, "title is required")

            testGrade = data.get('testGrade')
            if not testGrade:
                json_abort(400, "testGrade is required")

            concept = data.get('concept')
            if not concept:
                json_abort(400, "concept is required")

            schoolTest.text = title
            schoolTest.testGrade = testGrade
            schoolTest.concept = concept

            db.session.commit()

            return schoolTest

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        schoolTest = SchoolTest.query.filter_by(schoolTestID=id).first()

        if not schoolTest:
            json_abort(400, "School Test not found")
        else:
            db.session.delete(schoolTest)
            db.session.commit()

            return schoolTest

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)