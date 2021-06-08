from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False)
    country_code = db.Column(db.String(3), nullable=False)
    district = db.Column(db.String(20), nullable=False)
    population = db.Column(db.Integer, nullable=False)


class CitySchema(ma.Schema):
    class Meta:
        model = City
        fields = ('id', 'name', 'country_code', 'district', 'population')
