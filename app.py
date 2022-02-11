import flask as f
from pandas import DataFrame
from pickle import load


app = f.Flask(__name__)
model = load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return f.render_template("index.html")




@app.route("/predict", methods=["POST"])
def predict():
    A = []
    for i in f.request.form.values():
        A.append(int(i))
    predicted_profit = round(model.predict(DataFrame([[A[0], A[1]]]))[0][0],2)
    return f.render_template("result.html", pred= predicted_profit)


if __name__ == "__main__":
    app.run(debug=True)
