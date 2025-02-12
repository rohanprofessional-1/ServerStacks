import ansys.fluent.core as fluent
from ansys.fluent.core.filereader.case_file import CaseFile
import settings

import random as rd #temporary variable for generating data

def process_data_test(init_temp, speed):
    newT = rd.uniform(0, init_temp)
    newS = rd.uniform(0, speed)
    final_t = newT * newS
    return final_t, newT, newS

def process_data(init_temp, speed):
    session = fluent.launch_fluent(mode="solver")

    session.file.read_case(file_name=settings.CASE_MODEL)
    session.solver.tui.solve.initialize.compute_defaults()
    session.solver.tui.solve.iterate(1000)
    result_file_path = "path/to/save/results.cas"
    session.file.write_case(file_name=result_file_path)

    print(session.setup.boundary_conditions.velocity_inlet["inlet"].get_state())
    session.exit()
