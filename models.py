from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_image = "https://images-na.ssl-images-amazon.com/images/I/81S6UlXIJeL._SL1500_.jpg"

def connect_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()



class Pet(db.Model):
    """Pet Model """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=default_image)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

