from flask import Blueprint, render_template, request
from app.ml.predictor import predict_iris
from app.db.database import Database
from flask import redirect, url_for

bp = Blueprint("main", __name__)
db = Database()

@bp.route("/")
def home():
    stats = db.get_result_stats()
    records = db.get_all_iris()

    labels = [r[0] for r in stats]
    values = [r[1] for r in stats]

    return render_template(
        "index.html",
        labels=labels,
        values=values,
        records=records,
        result=None,
        input_data=None
    )
    
@bp.route("/predict", methods=["POST"])
def predict():
    sl = float(request.form["sl"])
    sw = float(request.form["sw"])
    pl = float(request.form["pl"])
    pw = float(request.form["pw"])

    result = predict_iris([sl, sw, pl, pw])

    db.save_iris(sl, sw, pl, pw, result)

    stats = db.get_result_stats()
    records = db.get_all_iris()

    labels = [r[0] for r in stats]
    values = [r[1] for r in stats]

    return render_template(
        "index.html",
        result=result,
        input_data={
            "sl": sl,
            "sw": sw,
            "pl": pl,
            "pw": pw
        },
        labels=labels,
        values=values,
        records=records
    )