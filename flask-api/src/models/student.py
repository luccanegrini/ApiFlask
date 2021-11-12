from . import db


class Student(db.Model):
    __tablename__ = 'student'

    studentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    created = db.Column(db.DateTime)
    courseID = db.Column(db.Integer, db.ForeignKey('course.courseID'))
    course = db.relationship('Course')
    age = db.Column(db.Integer)
    cpf = db.Column(db.Text())

    def __str__(self):
        return self.name

    def get_student_id(self):
        return self.studentID
