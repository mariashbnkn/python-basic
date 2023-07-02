from datetime import datetime
from pathlib import Path

from flask import request, flash
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import render_template

from models import db, Zodiacs, ZodiacBase
from sqlalchemy import and_

from .forms.listzodiac import ListZodiacForm

BASE_DIR = Path(__file__).resolve().parent

zodiacs_app = Blueprint(
    "zodiacs_app",
    __name__,
    url_prefix="/zodiacs",
)


@zodiacs_app.get("/", endpoint="list")
def get_zodiac_name_list():
    zodiacs: list[Zodiacs] = Zodiacs.query.order_by(Zodiacs.id).all()
    return render_template("zodiacs/list.html", zodiacs=zodiacs)


# if error
def get_name_list_by_id(zodiac_id: int) -> Zodiacs:
    return Zodiacs.query.get_or_404(
        zodiac_id,
        description=f"Zodiac #{zodiac_id} not found!"
    )


# get name id for link details
@zodiacs_app.get("/<int:zodiac_id>/", endpoint="details")
def get_zodiac_details(zodiac_id: int):
    zodiac = get_name_list_by_id(zodiac_id=zodiac_id)
    return render_template("zodiacs/details.html", zodiac=zodiac)


# func for get zodiac_base and compare
def zodiac_base_compare(date_bth_for_search: int):
    zodiac_base = ZodiacBase.query.filter(
        and_(ZodiacBase.first_date < date_bth_for_search,
             ZodiacBase.last_date > date_bth_for_search)).first()
    return zodiac_base


@zodiacs_app.route("/add/", methods=["GET", "POST"], endpoint="add") # нужно указать, какие методы поддерживаем
def create_new_zodiac():
    form = ListZodiacForm()
    if request.method == "GET":
        return render_template("zodiacs/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("zodiacs/add.html", form=form), 400

    date_bth = datetime.strptime(str(form.date.data), '%Y-%m-%d')
    date_bth_for_search = int(str(date_bth).replace('-', '')[4:-9])
    zodiac_base = zodiac_base_compare(date_bth_for_search)
    zodiac = Zodiacs(name=form.data["name"], date_bth=date_bth, id_zodiac=zodiac_base.id, zodiac_name=zodiac_base.name)
    db.session.add(zodiac)
    db.session.commit()
    url = url_for("zodiacs_app.details", zodiac_id=zodiac.id)
    flash(f"Created zodiac {zodiac.name!r}", category="success")
    return redirect(url)


@zodiacs_app.route(
    "/<int:zodiac_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_zodiac(zodiac_id: int):
    zodiac = get_name_list_by_id(zodiac_id=zodiac_id)
    if request.method == "GET":
        return render_template("zodiacs/confirm-delete.html", zodiac=zodiac)
    db.session.delete(zodiac)
    db.session.commit()
    flash(f"Deleted zodiac {zodiac.name!r}", category="warning")
    url = url_for("zodiacs_app.list")
    return redirect(url)