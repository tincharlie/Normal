import flask as F
from pandas import DataFrame
from pickle import load

app = F.Flask(__name__)
model = load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return F.render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    A = []
    for i in F.request.form.values():
        A.append(int(i))
    pred_profit = round(model.predict(DataFrame([[A[0]]]))[0][0], 2)

    return F.render_template("result.html", pred=pred_profit)


if __name__ == "__main__":
    app.run(debug=True)
