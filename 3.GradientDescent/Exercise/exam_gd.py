import numpy as np
import pandas as pd
from pyparsing import line
from sklearn import linear_model
import math


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.0002
    cost_previous = cost = 0

    for i in range(iterations):
        if i % 100000 == 0:
            print("\t From Gradient Descent : m {}, b {}, cost {} iteration {}".format(
                m_curr, b_curr, cost, i))
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val**2 for val in (y - y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
    print("From Gradient Descent : m {}, b {}, cost {} iteration {}".format(
        m_curr, b_curr, cost, i))


df = pd.read_csv('test_scores.csv')
gradient_descent(df['math'], df['cs'])
reg = linear_model.LinearRegression()
reg.fit(df[['math']].values, df[['cs']].values)
print(f"From sklearn Linear regression m: {reg.coef_} b:{reg.intercept_}")
