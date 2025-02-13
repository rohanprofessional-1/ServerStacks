import numpy as np
import pandas as pd
from scipy.optimize import minimize
from processing import process_data


def optimize(velocity, initial_temperature):
    return process_data(velocity, initial_temperature)
def main(initial_temperature):
    initial_velocity = np.array(1.0)
    bounds = [(0.1, 10.0)]
    result = minimize(optimize, initial_velocity, args= (initial_temperature), method="L-BFGS-B", bounds=bounds)
    return result.x, result.fun

