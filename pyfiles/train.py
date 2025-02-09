import csv
from itertools import product
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
import joblib
from processing import process_data

headers = ['Initial_temperature', 'angle', 'speed', 'Final_temperature']

def create_dataset():
    lower_bound = 1.0
    upper_bound = 5.0
    num_points = 25
    precision = 1
    data = np.linspace(lower_bound, upper_bound, num_points)
    dataT, dataA, dataS = np.round(data, precision), np.round(data, precision), np.round(data, precision)
    combinations = list(product(dataT, dataA, dataS))
    dataset_csv = 'results.csv'
    with open(dataset_csv, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(len(combinations)):
            dataT, dataA, dataS = combinations[i]
            finalTemperature = process_data(dataT, dataA, dataS)
            row = [dataT, dataA, dataS, finalTemperature]
            writer.writerow(row)

def train_model():
    results = pd.read_csv('results.csv')
    X = results[headers[0:len(headers) - 1]]
    y = results[['Final_temperature']]
    ridge_model = Ridge(alpha=1.0)
    ridge_model.fit(X, y)
    joblib.dump(ridge_model, '../models/predict_server_temp.joblib')
    print("Model successfully trained")

if __name__ == '__main__':
    create_dataset()
    train_model()
