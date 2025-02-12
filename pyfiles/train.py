import csv
from itertools import product
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
import joblib
from processing import process_data
import settings


def create_dataset():
    lower_bound = 1.0
    upper_bound = 5.0
    num_points = 25
    precision = 1
    data = np.linspace(lower_bound, upper_bound, num_points)
    dataT, dataS = np.round(data, precision), np.round(data, precision)
    combinations = list(product(dataT, dataS))
    with open(settings.DATASET, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(settings.HEADERS)
        for i in range(len(combinations)):
            dataT, dataS = combinations[i]
            finalTemperature = process_data(dataT, dataS)
            row = [dataT, dataS, finalTemperature]
            writer.writerow(row)

def train_model():
    results = pd.read_csv(settings.DATASET)
    X = results[settings.HEADERS[0:len(settings.HEADERS) - 1]]
    y = results[['Final_temperature']]
    ridge_model = Ridge(alpha=1.0)
    ridge_model.fit(X, y)
    joblib.dump(ridge_model, settings.MODEL)
    print("Model successfully trained")

def predict_model(input_temp, input_angle):
    model = joblib.load(settings.MODEL)
    return model.predict([input_temp, input_angle])



