#!/bin/bash

# Unzip two downloaded google drive folders, place in single folder
tar -xvf ./data/NYC*.zip -C ./data
tar -xvf ./data/Raw*.zip -C ./data
mv ./data/'NYC Raw Bike Share Data'/* ./data/RawBikeData2
rm -rf ./data/'NYC Raw Bike Share Data'

# Place raw files in new directory, rename files so that they have a consistent name format. 
mkdir ./data/dock_counts
for dir in ./data/RawBikeData2/*; 
do 
	echo ./data/dock_counts/counts_${dir:20:4}_${dir:25:2}.csv
	mv $dir/bikeshare_nyc_raw.csv ./data/dock_counts/counts_${dir:20:4}_${dir:25:2}.csv
done

# Remove unneeded directory
rm -rf ./data/RawBikeData2