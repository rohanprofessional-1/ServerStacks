# get started with case and data loaded
import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples
import pandas as pd
from tabulate import tabulate
solver = pyfluent.launch_fluent(start_transcript=False)
import_case = examples.download_file(
    file_name="exhaust_system.cas.h5", directory="pyfluent/exhaust_system"
)
import_data = examples.download_file(
    file_name="exhaust_system.dat.h5", directory="pyfluent/exhaust_system"
)
solver.file.read_case_data(file_name=import_case)
# check the active report plot monitors using the settings relevant object
sorted(solver.settings.solution.monitor.report_plots())
[
    "mass-bal-rplot",
    "mass-in-rplot",
    "mass-tot-rplot",
    "point-vel-rplot",
]
# initialize so that monitors object is usable
solver.solution.initialization.hybrid_initialize()
# check which monitors are available
sorted(solver.monitors.get_monitor_set_names())
[
   "mass-bal-rplot",
   "mass-in-rplot",
   "mass-tot-rplot",
   "point-vel-rplot",
   "residual"
]
# create and register a callback function that will
def display_monitor_table(monitor_set_name="mass-bal-rplot"):
    def display_table():
        data = solver.monitors.get_monitor_set_data(monitor_set_name=monitor_set_name)
        # extract iteration numbers
        iterations = data[0]
    
        # filter out additional callbacks
        if len(iterations) > display_table.iter_count:
            display_table.iter_count = len(iterations)
            # extract results
            results = data[1]
            # create a DataFrame
            df = pd.DataFrame(results, index=iterations)
            df.index.name = 'Iteration'
            df.reset_index(inplace=True)
            # The streamed data contains duplicates, so eliminate them
            df = df.drop_duplicates(subset='Iteration')
            print(tabulate(df, headers='keys', tablefmt='psql'))
        display_table.iter_count = 0
    return display_table


register_id = solver.monitors.register_callback(display_monitor_table())
# run the solver and see the full tabulated monitor data on each iteration
solver.solution.run_calculation.iterate(iter_count=10)