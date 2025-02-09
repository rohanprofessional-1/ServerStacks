import numpy as np
import pandas as pd
import joblib
from scipy.optimize import minimize
from processing import process_data


def optimize(X):
    model = joblib.load('/Users/rohannair/PycharmProjects/ServerStacks/models/predict_server_temp.joblib')
    feature_names = ["Initial_temperature", "angle", "speed"]
    X = np.array(X).reshape(1, -1)
    X = pd.DataFrame(X, columns=feature_names)
    return model.predict(X)[0]
def main():
    read_pd = pd.read_csv('results.csv')
    init_temp = np.mean(np.array(read_pd['Initial_temperature']), axis=0)
    init_angle = np.mean(np.array(read_pd['angle']), axis=0)
    init_speed = np.mean(np.array(read_pd['speed']), axis=0)
    X0 = np.array([init_temp, init_angle, init_speed])
    bounds = [(0, 5), (0, 5), (0,5)]
    result = minimize(optimize, X0, method="L-BFGS-B", bounds=bounds)
    return result.x, result.fun, result.success, result.message, result.nit
if __name__ == '__main__':
    print(main())
