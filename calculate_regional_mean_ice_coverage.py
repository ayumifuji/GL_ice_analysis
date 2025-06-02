# Import libraries
import xarray as xr
from shapely.geometry import Polygon, Point
import numpy as np
from datetime import date, timedelta


# Open GLSEA ice file - this can be any date
dir='glsea_datafiles/'
filename=dir+'2024_020_glsea_ice.nc'
file=xr.open_dataset(filename)


# specific area to focus, by longitude & latitude 
coordinates = [(-84.07, 43.56), (-84.07, 44.09), (-83.26, 44.09), (-83.36, 43.56) ]
polygon = Polygon(coordinates)


#print(file['ice_concentration'].values[0,:,:].shape)
#print(file['ice_concentration'].lon.values.shape)
#print(file['ice_concentration'].lat.values.shape)

# First, create a boolean array that defines mask for the area to focus (defined by coordiantes & polygon above) 
mask_array = np.ones(file['ice_concentration'].values[0,:,:].shape, dtype=bool)


# loop through indices
for jj in range(len(file['ice_concentration'].lat.values)):
	for ii in range(len(file['ice_concentration'].lon.values)):

		point = ( file['ice_concentration'].lon.values[ii], file['ice_concentration'].lat.values[jj] )

		if polygon.contains(Point(file['ice_concentration'].lon.values[ii], file['ice_concentration'].lat.values[jj])):
			mask_array[jj,ii] = True
		else:
			mask_array[jj,ii] = False


# Next, loop through each day and calculate spatial mean ice coverage for the area to focus

start_date = date(2023,11, 1)
end_date = date(2025, 5, 1)
delta = timedelta(days=1)

current_date = start_date


# open text file for outputs and write a header
with open("mean_ice_coverage_for_SaginawBay.txt", "w") as out_file:
       out_file.write("date, mean_ice_coverage [%]\n")
out_file.close()

while current_date <= end_date:
	
	# open a file for a given day
	filename=dir+str(current_date.year)+'_'+current_date.strftime("%j")+'_glsea_ice.nc'

	# if a file exist
	try:
		file=xr.open_dataset(filename)

		# create masked ice data array using the created boolean mask array
		masked_ice_data = np.where( mask_array, file['ice_concentration'].values[0,:,:], np.nan)

		#calculate mean ice coverage for the area to focus for the day
		mean_ice_coverage = np.nanmean(masked_ice_data)

		# write the result
		#print(current_date, mean_ice_coverage )
		with open("mean_ice_coverage_for_SaginawBay.txt", "a") as out_file:
			out_file.writelines(str(current_date)+", "+str(mean_ice_coverage)+"\n")
		out_file.close()

	# if a file does not exist
	except:
		print("A file not found: ", current_date)



	# add a day
	current_date += delta










