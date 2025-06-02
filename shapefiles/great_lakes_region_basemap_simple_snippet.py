# Snippet of code for including shapefiles.map
#
# Required variables
# ax        = your matplotlib subplot (NOTE: with a projection and extent applied)
# ccrs      = the cartopy.crs module
# Reader    = is included in the above modules and you shouldn't require an additional import
#
# Additional notes: The file paths given are based on the directory that the .nc file was in from the
# original script plot_aice.py. The file paths in this snippet have been converted to operate with
# Windows and may need to be updated for Mac/Linux use. The shapefiles required are located in the
# zip file great_lakes_region_basemap_simple.zip. All file types (.shp, .dbf, .sbx, etc.) are required 
# by cartopy to process and display.
  

### In my example, I placed this code after defining the colormap and before defining the colorbar

    canada = dir + 'work/province.shp'
    ax.add_geometries(Reader(canada).geometries(),
                    ccrs.PlateCarree(), edgecolor = 'gray', facecolor='w')
    
    us = dir + 'work/states_final.shp'
    ax.add_geometries(Reader(us).geometries(),
                    ccrs.PlateCarree(), edgecolor = 'gray', facecolor='w')
    
    rivers = dir + 'work/rivers_final.shp'
    ax.add_geometries(Reader(rivers).geometries(),
                    ccrs.PlateCarree(), edgecolor = 'blue', facecolor='None')
    
    rivers2 = dir + 'work/rivers_2_final.shp'
    ax.add_geometries(Reader(rivers2).geometries(),
                    ccrs.PlateCarree(), edgecolor = 'blue', facecolor='None')  