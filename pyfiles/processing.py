import ansys.fluent.core as fluent
import ansys.fluent.visualization as vis
from ansys.fluent.core.filereader.case_file import CaseFile
from ansys.fluent.core.filereader.data_file import DataFile
import numpy as np

def process_data(velocity, initial_temp):
    session = fluent.launch_fluent(mode="solver")
    path = r"C:\Users\snair322\OneDrive - Georgia Institute of Technology\2 projects\ServerStacks\models\with_ducting_with_names_mesh_file.cas.h5"
    
    session.file.read_case(file_name=path)
    session.setup.boundary_conditions.velocity_inlet["fluid_inlet"].momentum.velocity = velocity 
    session.setup.boundary_conditions.velocity_inlet["fluid_inlet"].thermal.t = initial_temp
    session.settings.solution.report_definitions.volume["max-temp"] = {}
    session.settings.solution.report_definitions.volume["max-temp"].report_type = "volume-average"
    session.settings.solution.report_definitions.volume["max-temp"].field = "temperature"
    session.settings.solution.report_definitions.volume["max-temp"].cell_zones = ["server_1"]

    session.solution.run_calculation.iterate(iter_count=1)
 
    session.file.write_case_data(file_name="output.cas.h5")
    session.exit()
    new_session = fluent.launch_fluent(mode="solver")
    new_session.file.read_case_data(file_name=r"C:\Users\snair322\OneDrive - Georgia Institute of Technology\2 projects\ServerStacks\pyfiles\output.cas.h5")
    solution_variable_data = new_session.fields.solution_variable_data.get_data(solution_variable_name="SV_T", zone_names=["server_1", "server_2", "server_3"])
    solution_variable_data.zones
    server1 = solution_variable_data.data['server_1']#add .data here to get it
    max_1 = max(server1) 
    server_2 = solution_variable_data.data['server_2']
    max_2 = max(server_2)
    server_3 = solution_variable_data.data['server_3']
    max_3 = max(server_3)
    return max(max_1, max_2, max_3)

print(process_data(2, 253))
