import numpy as np
from sklearn.model_selection import learning_curve

def gradient_descent(x, y):
    mi = bi = 0
    iterations = 3000
    n = len(x)
    learning_rate = 0.082

    for i in range(iterations):
        y_predicted = mi * x + bi
        cost = (1/n)*sum([val**2 for val in (y - y_predicted)])
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n)*sum((y - y_predicted))
        mi = mi - learning_rate * md 
        bi = bi - learning_rate * bd 
        print(f"Iteration: {i} m = {mi} b = {bi} cost = {cost}")



x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)