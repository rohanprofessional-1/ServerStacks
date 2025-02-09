#import ansys.core.fluent as fluent
import random as rd #temporary variable for generating data

def process_data(init_temp, angle, speed):
    newT = rd.uniform(0, init_temp)
    newA = rd.uniform(0, angle)
    newS = rd.uniform(0, speed)
    final_t = newT * newA * newS
    return final_t
