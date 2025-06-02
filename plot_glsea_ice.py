
# Import libraries
import cartopy.crs as ccrs
import matplotlib as mpl
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.feature as creature
from cartopy.io.shapereader import Reader


# Open GLSEA ice file
dir='glsea_datafiles/'
filename=dir+'2024_020_glsea_ice.nc'
file=xr.open_dataset(filename)


# specific area to focus, by longitude & latitude 
zoom_extent = [-84.07, -83.26, 43.56, 44.09]


# shapefiles for background geography information
canada = 'shapefiles/province.shp'
us = 'shapefiles/states_final.shp'
rivers = 'shapefiles/rivers_final.shp'
rivers2 = 'shapefiles/rivers_2_final.shp'


# plot a map
fig, ax = plt.subplots(2, 1, subplot_kw=dict(projection=ccrs.PlateCarree()),figsize=(4,6))

# first row - the whole Great Lakes
file['ice_concentration'].plot(
    ax=ax[0],
    transform=ccrs.PlateCarree(),  # this is important!
    # usual xarray stuff
    cbar_kwargs={"orientation": "horizontal", "shrink": 0.5},
    robust=True,
)

# Add gridlines and labels
gl = ax[0].gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_right = False

# background geography
ax[0].add_geometries(Reader(canada).geometries(),
            ccrs.PlateCarree(), edgecolor = 'gray', facecolor='w')
ax[0].add_geometries(Reader(us).geometries(),
                    ccrs.PlateCarree(), edgecolor = 'gray', facecolor='w')
#ax[0].add_geometries(Reader(rivers).geometries(),
#                    ccrs.PlateCarree(), edgecolor = 'blue', facecolor='None')
#ax[0].add_geometries(Reader(rivers2).geometries(),
#                    ccrs.PlateCarree(), edgecolor = 'blue', facecolor='None')  


# second row - the zoomed area
file['ice_concentration'].plot(
    ax=ax[1],
    transform=ccrs.PlateCarree(),  # this is important!
    # usual xarray stuff
    cbar_kwargs={"orientation": "horizontal", "shrink": 0.5},
    robust=True,
)

# Add gridlines and labels
gl = ax[1].gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_right = False

ax[1].set_extent(zoom_extent) # zoom over a specific area

# background geography
ax[1].add_geometries(Reader(canada).geometries(),
            ccrs.PlateCarree(), edgecolor = 'gray', facecolor='w')
ax[1].add_geometries(Reader(us).geometries(),
                    ccrs.PlateCarree(), edgecolor = 'gray', facecolor='w')
ax[1].add_geometries(Reader(rivers).geometries(),
                    ccrs.PlateCarree(), edgecolor = 'blue', facecolor='None')
ax[1].add_geometries(Reader(rivers2).geometries(),
                    ccrs.PlateCarree(), edgecolor = 'blue', facecolor='None')


# resolution too low
#ax[1].background_img(name='ne_shaded', resolution='low')
                   




plt.show()


