from main import db


class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    dl = db.relationship('CatsPosition', backref='cats', uselist=False)


class CatsPosition(db.Model):
    __tablename__ = 'catsPosition'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_add = db.Column(db.Date, nullable=False)
    date_change = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    cats_id = db.column(db.Integer, db.ForeignKey('cats.id'))


db.create_all()


def addCat(name, breed, gender, color, age):
    cat = Cats(name=name, breed=breed, gender=gender, color=color, age=age)
    db.session.add(cat)
    db.session.commit()

def getAllCats():
    return Cats.query.all()
def getOneCat(id):
    return Cats.query.filter_by(id=id).all()

def addCatPosition(date_add, date_change, cost, cats_id):
    cat = CatsPosition(date_add=date_add, date_change=date_change, cost=cost, cats_id=cats_id)
    db.session.add(cat)
    db.session.commit()

def getAllCatsPosition():
    return CatsPosition.query.all()
def getOneCatPosition(id):
    return CatsPosition.query.filter_by(id=id).all()