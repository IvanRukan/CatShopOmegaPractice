from UserModels import db


class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    cats_position = db.relationship('CatsPosition', back_populates='cats', cascade='save-update, merge, delete')


class CatsPosition(db.Model):
    __tablename__ = 'catsPosition'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    cats_id = db.Column(db.Integer, db.ForeignKey('cats.id'), nullable=False, index=True)
    cats = db.relationship('Cats', back_populates='cats_position')


def add_cat(name, breed, gender, color, age):
    cat = Cats(name=name, breed=breed, gender=gender, color=color, age=age)
    db.session.add(cat)
    db.session.commit()


def get_all_cats():
    return Cats.query.all()


def get_one_cat(id):
    return Cats.query.filter_by(id=id).all()


def add_cat_position(date, cost, cats_id):
    cat = CatsPosition(date=date, cost=cost, cats_id=cats_id)
    db.session.add(cat)
    db.session.commit()


def get_all_cats_position():
    return CatsPosition.query.all()


def get_one_cat_position(id):
    return CatsPosition.query.filter_by(id=id).all()