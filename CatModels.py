from main import db


class Cats(gitdb.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)


class CatsPosition(db.Model):
    __tablename__ = 'catsPosition'
    id = db.Column(db.Integer, primary_key=True)
    date_add = db.Column(db.Date, nullable=False)
    date_change = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    cats_id = db.column(db.Integer, db.ForeignKey('cats.id'))


db.create_all()
