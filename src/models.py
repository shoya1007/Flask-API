from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import enum

db = SQLAlchemy()
ma = Marshmallow()


class ContientType(str, enum.Enum):
    Asia = 'Asia',
    Europe = 'Europe',
    NorthAmerica = 'North America',
    Africa = 'America',
    Oceania = 'Oceania',
    Antarcticia = 'Antarcticia',
    SouthAmerica = 'South America'


class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), nullable=False)
    country_code = db.Column(db.String(3), db.ForeignKey(
        'country.code'), nullable=False)
    district = db.Column(db.String(20), nullable=False)
    population = db.Column(db.Integer, nullable=False)


class CitySchema(ma.Schema):
    class Meta:
        model = City
        fields = ('id', 'name', 'country_code', 'district', 'population')


class Country(db.Model):
    __tablename__ = 'country'

    code = db.Column(db.String(3), nullable=False, primary_key=True)
    name = db.Column(db.String(52), nullable=False)
    continent = db.Column(db.Enum(ContientType), nullable=False)
    region = db.Column(db.String(26), nullable=False)
    surface_area = db.Column(db.Float, nullable=False)
    indep_year = db.Column(db.Integer)
    population = db.Column(db.Integer, nullable=False)
    life_expectancy = db.column(db.Float)
    gnp = db.Column(db.Float)
    gnp_old = db.Column(db.Float)
    local_name = db.Column(db.String(45), nullable=False)
    government_form = db.Column(db.String(45), nullable=False)
    head_of_state = db.Column(db.String(60), nullable=False)
    capital = db.Column(db.String(11), nullable=False)
    code2 = db.Column(db.String(2), nullable=False)
    cities = db.relationship('City', backref='country', lazy=True)


class CountrySchema(ma.Schema):
    class Meta:
        model = Country
        fields = ('code', 'name', 'continent', 'region', 'surface_area', 'indep_year', 'population',
                  'life_expectancy', 'gnp', 'gnp_old', 'local_name', 'government_form', 'head_of_state', 'capital', 'code2')
