from processing import process_data_test
from optimize import minArgs
from train import train_model
THRESHOLD = 1.0
def check_threshold(user_temp, user_velocity):
    actual_Ft, input_temp, input_velocity = process_data_test(user_temp, user_velocity)
    model_Ft, opt_temp, opt_velocity = minArgs(user_temp, user_velocity)
    if abs(actual_Ft - model_Ft) < THRESHOLD:
        return True, model_Ft, opt_temp, opt_velocity
    else:
        return False, actual_Ft, input_temp, input_velocity

