from processing import process_data_test
from optimize import minArgs
from train import train_model
import csv
import settings


def check_threshold(user_temp, user_velocity):
    actual_Ft, input_temp, input_velocity = process_data_test(user_temp, user_velocity)
    model_Ft, opt_temp, opt_velocity = minArgs(user_temp, user_velocity)
    if abs(actual_Ft - model_Ft) < settings.THRESHOLD:
        return True, model_Ft, opt_temp, opt_velocity
    else:
        with open(settings.DATASET, 'a') as f:
            writer = csv.writer(f)
            row = [input_temp, input_velocity, actual_Ft]
            writer.writerow(row)
        return False, actual_Ft, input_temp, input_velocity

