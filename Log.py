from CatModels import db

class LogsModel(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_operation = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)
    type_user = db.Column(db.String(80), nullable=False)

def add_log(type_operation, date, type_user):
    db.session.add(LogsModel(type_operation=type_operation, date=date,type_user=type_user))
    db.session.commit()

def get_log_period_time(date_start, date_end):
    return LogsModel.query.filter(date_start <= LogsModel.date <= date_end)