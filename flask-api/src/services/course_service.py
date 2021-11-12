from src.models import db
from src.models.course import Course
from src.config.restplus import json_abort
from sqlalchemy.exc import SQLAlchemyError


def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400, "Name is required")

        studyArea = data.get('studyArea')
        if not studyArea:
            json_abort(400, "Study area is required")

        course = Course(name=name, studyArea=studyArea)
        db.session.add(course)
        db.session.commit()

        return course

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        course = Course.query.filter_by(courseID=id).first()

        if not course:
            json_abort(400, "Course not found")
        else:
            return course

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def getAll():
    try:
        courses = Course.query.all()
        return courses

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def put(id, data):
    try:

        course = Course.query.filter_by(courseID=id).first()

        if not course:
            json_abort(400, "Student not found")
        else:
            name = data.get('name')
            if not name:
                json_abort(400, "Name is required")

            studyArea = data.get('studyArea')
            if not studyArea:
                json_abort(400, "Study Area is required")

            course.name = name
            course.studyArea = studyArea

            db.session.commit()

            return course

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        course = Course.query.filter_by(courseID=id).first()

        if not course:
            json_abort(400, "Course not found")
        else:
            db.session.delete(course)
            db.session.commit()

            return course

    except SQLAlchemyError as err:
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)