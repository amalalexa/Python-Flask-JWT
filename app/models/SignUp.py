from database import db


class SignUp(db.Model):
    __tablename__ = 'sign_up'

    sign_up_id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    user_id = db.Column(db.String)

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def order_data(cls):
        return cls.query.group_by(cls.sign_up_id)

    def commit_data(self):
        db.session.add(self)
        db.session.commit()