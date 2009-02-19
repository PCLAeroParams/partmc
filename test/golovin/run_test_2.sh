#!/bin/bash

# make sure that the current directory is the one where this script is
cd ${0%/*}

../../extract_summary_aero mass out/golovin_mc_0001.nc out/golovin_mc_mass.txt
../../extract_summary_aero mass out/golovin_exact_0001.nc out/golovin_exact_mass.txt

../../numeric_diff out/golovin_mc_mass.txt out/golovin_exact_mass.txt 0 2e-2
exit $?