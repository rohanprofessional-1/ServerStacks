import ansys.fluent.core as fluent

def process_data(velocity, initial_temp):
    session = fluent.launch_fluent(mode="solver")
    path = r"C:\Users\snair322\OneDrive - Georgia Institute of Technology\2 projects\ServerStacks\models\with_ducting_fluent_meshing.cas 1.h5"
   
    session.file.read_case(file_name=path)
    session.setup.boundary_conditions.velocity_inlet["fluid_inlet"].momentum.velocity = velocity 
    session.setup.boundary_conditions.velocity_inlet["fluid_inlet"].thermal.t = initial_temp
    
    #session.solution.run_calculation.iterate(iter_count=75)

    server_report1 = session.solution.monitor.report_files.create(
        name="server1_report",
    )
    field_data = session.fields.field_data.get_scalar_field_data("temperature", surfaces=["wall_server_top_r_3"])
    print(field_data)
    

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

    
    server1_temp = session.solution.report_definitions.compute(server_report1.get_data().data[0])
    server2_temp = session.solution.report_definitions.compute(server_report2.get_data().data[0])
    server3_temp = session.solution.report_definitions.compute(server_report3.get_data().data[0])
    return max(server1_temp, server2_temp, server3_temp)

process_data(2, 253)
