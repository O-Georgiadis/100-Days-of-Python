from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.exc import IntegrityError
from pathlib import Path
from random import randint

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
db_path = Path(__file__).parent/"instance/cafes.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "map_url": self.map_url,
                "img_url": self.img_url,
                "location": self.location,
                "seats": self.seats,
                "has_toilet": self.has_toilet,
                "has_wifi": self.has_wifi,
                "has_sockets": self.has_sockets,
                "can_take_calls": self.can_take_calls,
                "coffee_price": self.coffee_price,
            }
    
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random():
    shop_id = randint(1, Cafe.query.count())
    shop_selected = db.get_or_404(Cafe, shop_id)
    return jsonify(cafes=shop_selected.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    

@app.route("/add", methods=["POST"])
def add_cafe():
    def to_bool(value):
        if value is None:
            return False
        v = str(value).strip().lower()
        if v in {"1", "true", "t", "yes", "y", "on"}:
            return True
        if v in {"0", "false", "f", "no", "n", "off", ""}:
            return False
        return bool(value)
    new_cafe = Cafe(
                name = request.form.get("name"),
                map_url = request.form.get("map_url"),
                img_url = request.form.get("img_url"),
                location = request.form.get("location"),
                seats = request.form.get("seats"),
                has_toilet = to_bool(request.form.get("has_toilet")),
                has_wifi = to_bool(request.form.get("has_wifi")),
                has_sockets = to_bool(request.form.get("has_sockets")),
                can_take_calls = to_bool(request.form.get("can_take_calls")),
                coffee_price = request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(error={"Conflict": "A cafe with this name already exists."}), 409
    return jsonify(response={"success": "Successfully added the new cafe."}), 201


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
