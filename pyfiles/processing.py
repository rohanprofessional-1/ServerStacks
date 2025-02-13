import ansys.fluent.core as fluent

def process_data(velocity, initial_temp):
    session = fluent.launch_fluent(mode="solver")
    path = r"C:\Users\snair322\OneDrive - Georgia Institute of Technology\2 projects\ServerStacks\models\with_ducting_with_names_mesh_file.cas.h5"
    session.file.read_case(file_name=path)
    session.setup.boundary_conditions.velocity_inlet["fluid_inlet"].momentum.velocity = velocity 
    session.setup.boundary_conditions.velocity_inlet["fluid_inlet"].thermal.t = initial_temp

    server_report1 = session.solution.monitor.report_files.create(
        name="server1_report",
        surface_names=["interior-server_1"],
        field="temperature"
    )

    server_report2 = session.solution.monitor.report.create(
        "surface-massavg",
        name="server1_report",
        surface_names=["interior-server_2"],
        field="temperature"
    )

    server_report3 = session.solution.monitor.report.create(
        "surface-massavg",
        name="server1_report",
        surface_names=["interior-server_3"],
        field="temperature"
    )

    session.solution.run_calculation.iterate(iter_count=75)
    
    server1_temp = session.solution.report_definitions.compute(server_report1.get_data().data[0])
    server2_temp = session.solution.report_definitions.compute(server_report2.get_data().data[0])
    server3_temp = session.solution.report_definitions.compute(server_report3.get_data().data[0])
    return max(server1_temp, server2_temp, server3_temp)

process_data(2, 253)
