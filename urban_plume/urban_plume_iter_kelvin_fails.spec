run_type mc                     # Monte Carlo run
output_prefix out/urban_plume_no_coag   # prefix of output files
state_prefix out/urban_plume_no_coag_state # prefix of state files
process_spec process.dat        # processing specification
n_loop 1                        # number of Monte Carlo loops
n_part 1000                   # total number of particles
kernel brown                    # coagulation kernel

t_max 86400                     # total simulation time (s)
del_t 60                        # timestep (s)
t_output 3600                   # output interval (0 disables) (s)
t_state 0                       # state output interval (0 disables) (s)
t_state_netcdf 3600             # NetCDF state output interval (0 disables) (s)
t_progress 600                  # progress printing interval (0 disables) (s)

n_bin 160                       # number of bins
r_min 1e-10                      # minimum radius (m)
r_max 1e-5                      # maximum radius (m)

gas_data gas_data.dat           # file containing gas data
gas_init gas_init_LA.dat           # initial gas concentrations

aerosol_data aero_data.dat      # file containing aerosol data
aerosol_init aero_init_dist_LA_low.dat # aerosol initial condition file

temp_profile temp_LA.dat         # temperature profile file
height_profile height_LA_2.dat     # height profile file
gas_emissions gas_emit_LA_NH3.dat    # gas emissions file
gas_background gas_back_LA.dat   # background gas concentrations file
aero_emissions aero_emit_LA_highC.dat  # aerosol emissions file
aero_background aero_back_LA_low.dat # aerosol background file

rel_humidity 0.85               # initial relative humidity (1)
pressure 1e5                    # initial pressure (Pa)
latitude 40                     # latitude (degrees, -90 to 90)
longitude 0                     # longitude (degrees, -180 to 180)
altitude 0                      # altitude (m)
start_time 21600                # start time (s since 00:00 UTC)
start_day 200                   # start day of year (UTC)

rand_init 8                     # random initialization (0 to use time)
mix_rate 0                      # mixing rate between processes (0 to 1)
do_coagulation no               # whether to do coagulation (yes/no)
allow_double yes                # whether to allow doubling (yes/no)
do_condensation no              # whether to do condensation (yes/no)
do_mosaic yes                   # whether to do MOSAIC (yes/no)
do_restart no                   # whether to restart from stored state (yes/no)
restart_name XXXX.d             # filename to restart from