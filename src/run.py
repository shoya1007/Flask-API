from flask import Flask
from api import api
from models import db

app = Flask(__name__)

app.register_blueprint(api)

# DB初期化
db.init_app(app)

if __name__ == '__main__':
    app.run()
