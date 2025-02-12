import numpy as np
import pandas as pd
import joblib
from scipy.optimize import minimize



def optimize(X):
    model = joblib.load('models/predict_server_temp.joblib')
    feature_names = ["Initial_temperature", "speed"]
    X = np.array(X).reshape(1, -1)
    X = pd.DataFrame(X, columns=feature_names)
    return model.predict(X)[0]
def minArgs(temperature, speed):
    init_temp = temperature
    init_speed = speed
    X0 = np.array([init_temp, init_speed])
    bounds = [(0, 5), (0, 5), (0,5)]
    result = minimize(optimize, X0, method="L-BFGS-B", bounds=bounds)
    return result.x, result.fun

