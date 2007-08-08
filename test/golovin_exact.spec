run_type exact                  # exact solution
output_file out/golovin_exact_summary.d # name of output file
num_conc 1e9                    # particle concentration (#/m^3)

t_max 600                       # total simulation time (s)
t_output 60                     # output interval (0 disables) (s)

n_bin 160                       # number of bins
r_min 1e-8                      # minimum radius (m)
r_max 1e-3                      # maximum radius (m)

gas_data gas_data_simple.dat    # file containing gas data
aerosol_data aerosol_data_water.dat # file containing aerosol data

temp_profile temp_constant_15C.dat # temperature profile file
height_profile height_constant_1km.dat # height profile file
gas_emissions gas_none_timed.dat # gas emissions file
gas_background gas_none_timed.dat # background gas concentrations file
aero_emissions aerosol_none_timed.dat # aerosol emissions file
aero_background aerosol_none_timed.dat # aerosol background file

rel_humidity 0.999              # initial relative humidity (1)
pressure 1e5                    # initial pressure (Pa)
air_density 1.25                # initial air density (kg/m^3)
latitude 40                     # latitude (degrees, -90 to 90)
longitude 0                     # longitude (degrees, -180 to 180)
altitude 0                      # altitude (m)
start_time 0                    # start time (s since 00:00 UTC)
start_day 1                     # start day of year (UTC)

soln golovin_exp                # solution type
mean_radius 1e-5                # mean radius (m)