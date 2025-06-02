import cartopy.crs as ccrs
import matplotlib as mpl
import matplotlib.pyplot as plt
import xarray as xr

dir='tmp/'
filename=dir+'2024_020_glsea_ice.nc'
file=xr.open_dataset(filename)

dimensions = dict(file.dims)
variables = file.variables
#attributes = file.attrs
#print(dimensions)
#print(" ")
#print(variables)
#print(" ")
#print(attributes)


# specific area to focus, by longitude & latitude 
zoom_extent = [-84.07, -83.26, 43.56, 44.09]


fig, ax = plt.subplots(2, 1, subplot_kw=dict(projection=ccrs.PlateCarree()),figsize=(4,6))


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

ax[0].coastlines()  # cartopy function



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

ax[1].coastlines()  # cartopy function
ax[1].set_extent(zoom_extent) # zoom over a specific area


plt.show()


