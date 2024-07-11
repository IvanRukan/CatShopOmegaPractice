from UserModels import db


class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    cats_position = db.relationship('CatsPosition', backref='cats', cascade='all, delete-orphan', lazy='dynamic')


class CatsPosition(db.Model):
    __tablename__ = 'catsPosition'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    cats_id = db.Column(db.Integer, db.ForeignKey('cats.id'), nullable=False)


def add_cat(name, breed, gender, color, age):
    cat = Cats(name=name, breed=breed, gender=gender, color=color, age=age)
    db.session.add(cat)
    db.session.commit()


def get_all_cats():
    return Cats.query.all()


def get_one_cat(id):
    try:
        cat = Cats.query.filter_by(id=id).all()[0]
    except IndexError:
        cat = 404
    return cat


def add_cat_position(date, cost, cats_id):
    cat = CatsPosition(date=date, cost=cost, cats_id=cats_id)
    db.session.add(cat)
    db.session.commit()


def get_all_cats_position():
    return CatsPosition.query.all()


def get_one_cat_position(id):
    try:
        cat = CatsPosition.query.filter_by(cats_id=id).all()[0]
    except IndexError:
        cat = 404
    return cat


def remove_cat(id):
    Cats.query.filter_by(id=id).delete()
    db.session.commit()


def remove_position(id):
    CatsPosition.query.filter_by(cats_id=id).delete()
    db.session.commit()


def update_cat_and_pos(id, name, breed, gender, color, age, date, cost):
    cat = get_one_cat(id)
    cat_pos = get_one_cat_position(id)
    cat.name = name
    cat.breed = breed
    cat.gender = gender
    cat.color = color
    cat.age = age
    cat_pos.date = date
    cat_pos.cost = cost
    db.session.commit()

