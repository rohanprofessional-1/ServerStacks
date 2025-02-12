import ansys.fluent.core as fluent
from ansys.fluent.core.filereader.case_file import CaseFile

import random as rd #temporary variable for generating data

def process_data_test(init_temp, angle, speed):
    newT = rd.uniform(0, init_temp)
    newA = rd.uniform(0, angle)
    newS = rd.uniform(0, speed)
    final_t = newT * newA * newS
    return final_t

def process_data(init_temp, angle, speed):
    meshing = fluent.launch_fluent(mode="meshing")
    try:
        meshing.file.read(file_name="")
        print("Mesh file imported successfully!")
    except Exception as e:
        print(f"Error importing mesh file: {e}")
   
  
process_data(0,0,0)