#!/bin/bash

# set start and end dates
date_start="2023-10-01"
date_end="2023-11-02"

#date_end="2025-06-01"
date_now=$date_start


# NOAA CoastWatch Great Lakes node THREDDS server
URL="https://apps.glerl.noaa.gov/thredds/fileServer/glsea_ice_nc/"


# loop through days 
while [[ $date_now != $date_end ]]; do

 # get year
 year=`date -j -f "%Y-%m-%d" $date_now "+%Y"`

 # get month
 month=`date -j -f "%Y-%m-%d" $date_now "+%m"`

 # if July - October, skip. Ice data files for these months are not provided.
 if [ "$month" -ge 6 ] && [ $month -le 10 ]; then
   echo "Skip. GLSEA data is not provided for June-Oct."

 # if November-May, download ice data files.
 else
 
  # get julian day (days since Jan 1 in each year)
  julian_day=`date -j -f "%Y-%m-%d" $date_now "+%j"`

  # full URL and file name to download
  fname=${URL}${year}"/"${month}"/"${year}"_"${julian_day}"_glsea_ice.nc"

  # download the file
  echo "Downloading " $fname "...."
  wget $fname

 fi


 # add a day
 date_now=`date -j -v +1d -f "%Y-%m-%d" $date_now +%Y-%m-%d`


done





