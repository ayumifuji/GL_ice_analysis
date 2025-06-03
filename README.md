# Great Lakkes  ice data analysis

This repo contains a set of scripts to download daily spatial ice concentration data files from Great Lakes Surface Environmental Analysis (GLSEA), plot spatial maps, calculate & creat timeseries of mean ice coverage over a select area (defined by a polygon), and conduct timeseries analyses.


## Scripts

- download.sh: A bash shell script to download GLESA daily ice data files from the THREDDS server. Start & end dates can be specified at the header.

- plot_glsea_ice.py: A python script to plot a spatial map of the GLESA daily ice data for a given day. Note that this script assumes a data file is included under the glsea_datafiles directory. This script also plots a spatial map of ice concentration over a Zoomed area (specified by lat & lon extent).

- calculate_regional_mean_ice_coverage.py: A python script to calculate mean ice coverage for a given area, defined by a polygon. The default is for Saginaw Bay. An output is a text file that include a timeseries of mean ice coverage.

-  


