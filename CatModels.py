from main import db


class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)


class CatsPosition(db.Model):
    __tablename__ = 'catsPosition'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_add = db.Column(db.Date, nullable=False)
    date_change = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    cats_id = db.column(db.Integer, db.ForeignKey('cats.id'))


def add_cat(name, breed, gender, color, age):
    cat = Cats(name=name, breed=breed, gender=gender, color=color, age=age)
    db.session.add(cat)
    db.session.commit()


def get_all_cats():
    return Cats.query.all()


def get_one_cat(id):
    return Cats.query.filter_by(id=id).all()


def add_cat_position(date_add, date_change, cost, cats_id):
    cat = CatsPosition(date_add=date_add, date_change=date_change, cost=cost, cats_id=cats_id)
    db.session.add(cat)
    db.session.commit()


def get_all_cats_position():
    return CatsPosition.query.all()


def get_one_cat_position(id):
    return CatsPosition.query.filter_by(id=id).all()