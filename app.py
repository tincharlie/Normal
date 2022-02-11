

import flask as f
from pandas import DataFrame
from pickle import load

# # Create a web application and load contents of pickle file

app = f.Flask(__name__)
model = load(open("model.pkl", "rb"))


# Load template on opening app home page

@app.route("/")
def home():
    return f.render_template("index.html")


# Create predictions and show it on page


@app.route("/predict", methods=["POST"])
def predict():
    A = []
    for i in f.request.form.values():
        A.append(int(i))
    predicted_profit = round(model.predict(DataFrame([[A[0], A[1]]]))[0][0],2)

    """
    # return f.render_template("index.html", pred= predicted_profit)
    If i will use index.html so itmeans the output will be on the same page.
    If i will use index.html and result.html  means output will print on the new page
    
    """

    return f.render_template("result.html", pred= predicted_profit)

# # Start the app

# In[ ]:


if __name__ == "__main__":
    app.run(debug=True)
