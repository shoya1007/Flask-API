from flask import Flask
from api import api
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# 文字化け対策
app.config['JSON_AS_ASCII'] = False

# DB初期化
db.init_app(app)

app.register_blueprint(api)

if __name__ == '__main__':
    app.run()
