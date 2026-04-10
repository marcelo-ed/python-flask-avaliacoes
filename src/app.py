from flask import Flask
from dotenv import load_dotenv
import os

from extensions import db
from routes import main


def create_app():
    app = Flask(__name__)

    load_dotenv()

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    name = os.getenv("DB_NAME")
    secret_key = os.getenv("SECRET_KEY")

    if password:
        uri = f"mysql+pymysql://{user}:{password}@{host}/{name}"
    else:
        uri = f"mysql+pymysql://{user}@{host}/{name}"

    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = secret_key

    db.init_app(app)
    app.register_blueprint(main)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
