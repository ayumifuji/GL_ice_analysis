# Great Lakes ice data analysis

This repo contains a set of scripts to download daily spatial ice concentration data files from Great Lakes Surface Environmental Analysis (GLSEA), plot spatial maps, calculate & creat timeseries of mean ice coverage over a select area (defined by a polygon), and conduct timeseries analyses.


## Scripts

- download.sh: A bash shell script to download GLESA daily ice data files from the THREDDS server. Start & end dates can be specified at the header. Note that GLSEA ice data files are available back to 1995. 

- plot_glsea_ice.py: A python script to plot a spatial map of the GLESA daily ice data for a given day. Note that this script assumes a data file is included under the glsea_datafiles directory. This script also plots a spatial map of ice concentration over a Zoomed area (specified by lat & lon extent).

- calculate_regional_mean_ice_coverage.py: A python script to calculate mean ice coverage for a given area, defined by a polygon. The default is for Saginaw Bay. An output is a text file that include a timeseries of mean ice coverage.

- timeseries_analysis.py: A Python script to read the text timeseries file calculated by calculate_regional_mean_ice_coverage.py, plot daily timeseries, overlay monthly mean timeseries & annual maximum values. 

## Directories
- glses_datafiles: This directory should contain downloaded GLSEA files. On the repo, it's empty (no data is stored, they need to be downloaded from the CoastWatch website).
- shapefiles: This directory contains geography shapefiles that are used by plot_glsea_ice.py. When plotting spatial maps, geography information, such as rivers and state boundaries, will be added based on these shapefiles. 


## Usage
### download.sh
 
Edit "date_start" and "date_end" in the header to specify the time range for which you'd like to download files.  
On a terminal, type below.

``` 
./download.sh
``` 

The date command currently used is for Mac. There's also an option for Linux bash. Comment out the lines for Mac and uncomment the lines for Linux bash if using Linux bash.

### plot_glsea_ice.py 

``` 
python plot_glsea_ice.py
``` 

### calculate_regional_mean_ice_coverage.py

```
python calculate_regional_mean_ice_coverage.py
```

### timeseries_analysis.py

```
python timeseries_analysis.py

```    


