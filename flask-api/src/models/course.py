from . import db


class Course(db.Model):
    __tablename__ = 'course'

    courseID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    studyArea = db.Column(db.Text())

    def __str__(self):
        return self.name

    def get_course_id(self):
        return self.courseID
