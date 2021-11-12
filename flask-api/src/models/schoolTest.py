from . import db


class SchoolTest(db.Model):
    __tablename__ = 'schoolTest'

    schoolTestID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID', ondelete='CASCADE'))
    student = db.relationship('Student')
    testGrade = db.Column(db.Float)
    concept = db.Column(db.Text())
    created = db.Column(db.DateTime)

    def __str__(self):
        return self.concept

    def get_student_id(self):
        return self.schoolTestID
