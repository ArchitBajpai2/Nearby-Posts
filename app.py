from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:archit2001@localhost/mydatabase'
db = SQLAlchemy(app)




def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:archit2001@localhost/mydatabase'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from posts.routes import posts_bp
    from weather.routes import weather

    app.register_blueprint(posts_bp)
    app.register_blueprint(weather)

    return app
