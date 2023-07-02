import json
from os import getenv

from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from models import ZodiacBase, db, Zodiacs
from views.zodiacs import zodiacs_app

app = Flask(__name__)
app.register_blueprint(zodiacs_app)

config_class_name = getenv("CONFIG_CLASS", "ProductionConfig")
config_object = f"config.{config_class_name}"
app.config.from_object(config_object)

db.init_app(app)

migrate = Migrate(app=app, db=db)

csrf = CSRFProtect(app)

path = './models/astro.json'


# add zodiac from json
def create_zodiac():
    with app.app_context():
        with open(path, 'r') as f:
            zodiacs = json.loads(f.read())
        for zodiac in zodiacs:
            zodiacal = ZodiacBase(
                id=zodiac.get('id'),
                first_date=zodiac.get('first_date'),
                last_date=zodiac.get('last_date'),
                name=zodiac.get('name'),
            )
            print(zodiac)
            db.session.add(zodiacal)
        db.session.commit()


def delete_zodiac_base():
    with app.app_context():
        db.session.query(ZodiacBase).delete()
        db.session.commit()


def delete_zodiacs():
    with app.app_context():
        db.session.query(Zodiacs).delete()
        db.session.commit()


@app.get("/", endpoint="index")
def hello_root():
    return render_template("index.html")


if __name__ == '__main__':
    # delete_zodiacs()
    # delete_zodiac_base()
    # create_zodiac()
    app.run(host="0.0.0.0", debug=True)
