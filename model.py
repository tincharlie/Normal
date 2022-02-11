from pickle import dump, load
from pandas import read_csv
from sklearn.linear_model import LinearRegression

A = read_csv("/Users/user/Desktop/python/datasets/50_Startups.csv")
X = A[["RND", "MKT"]]
Y = A[["PROFIT"]]


lm = LinearRegression()
model = lm.fit(X, Y)
dump(model, open("model.pkl", "wb"))
