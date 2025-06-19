# import libraries
import pandas as pd
import matplotlib.pyplot as plt


# read a text file that contains timeseries of mean ice coverage for an area of interest 
df=pd.read_csv("mean_ice_coverage_for_SaginawBay.txt")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date',inplace=True)

# print header
#print(df.head())
#print(df.info())

# create a figure
fig, ax = plt.subplots()


# plot daily timeseries
ax.plot_date(df.index, df[' mean_ice_coverage [%]'],'-',label="daily")

# create monthly average
monthly = df[' mean_ice_coverage [%]'].resample('MS',loffset=pd.Timedelta(15, 'd')).mean()
# use below for pandas earlier than 1.1.0 
#monthly = df[' mean_ice_coverage [%]'].resample('MS', loffset=pd.Timedelta(15, 'd')).mean()
ax.plot_date(monthly.index, monthly,'*-',label="monthly")
print(monthly)

# create annual average
annual_max = df[' mean_ice_coverage [%]'].resample('Y').max()
annual_max_index = df.groupby(pd.Grouper(freq='Y'))[' mean_ice_coverage [%]'].idxmax()
annual_max.index = annual_max_index

ax.plot_date(annual_max_index, annual_max,'o',markersize=12,label="annual maximum")
#print(annual_max)
ax.legend()

fig.autofmt_xdate()

plt.show()


