import logging

logging.basicConfig(level=logging.DEBUG)

from flask import Flask

from backend.db_connection import db

from backend.customers.customer_routes import customers
from backend.products.products_routes import products
from backend.social.social_routes import social
from backend.activity.activity_routes import activity
<<<<<<< HEAD
from backend.models.model_routes import models
=======
>>>>>>> 6082d2c70efd6268ada209d7203d2988fbff3a29
from backend.article_data.article_data import article
import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # Secret key that will be used for securely signing the session
    # cookie and can be used for any other security related needs by
    # extensions or your application
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Database configuration
    app.config["MYSQL_DATABASE_USER"] = os.getenv("DB_USER")
    app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_ROOT_PASSWORD")
    app.config["MYSQL_DATABASE_HOST"] = os.getenv("DB_HOST")
    app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("DB_PORT"))
    app.config["MYSQL_DATABASE_DB"] = os.getenv("DB_NAME")

    # Initialize the database object with the settings above.
    db.init_app(app)

    @app.route("/")
    def welcome():
        return "<h1>Welcome to the Algorithm Avenger's wonderful app!</h1>"

    @app.route("/test")
    def getData():
        data = {
            "user1": {
                "Name": "Mark Fontenot",
                "Course": "CS 3200",
            },
            "user2": {
                "Name": "Eric Gerber",
                "Course": "DS 3000",
            },
        }
        return data

    app.logger.info("current_app(): registering blueprints with app object.")
    app.register_blueprint(customers, url_prefix="/c")
    app.register_blueprint(products, url_prefix="/p")
    app.register_blueprint(social, url_prefix="/s")
    app.register_blueprint(activity, url_prefix="/a")
    app.register_blueprint(models, url_prefix="/models")
    app.register_blueprint(article, url_prefix='/article')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=4000)
