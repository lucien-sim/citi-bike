#!/bin/bash

# Extract data from .zip files. 
sh extract_station_counts.sh

# Create and fill SQL database for dock count data. 
python fill_citi_bike_database.py