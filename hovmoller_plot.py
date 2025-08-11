# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read a text file that contains timeseries of mean ice coverage for an area of interest 
# This time, we do not set 'date' as index as we use winter year (winter_year) and day of winter (dow) for y and x axes.
df=pd.read_csv("mean_ice_coverage_for_SaginawBay.txt")
df['date'] = pd.to_datetime(df['date'])


# derive winter year
df['witer_year'] = df['date'].apply(lambda d: d.year if d.month >= 11 else d.year - 1 )
# derive day of winter, i.e., days starting on Nov 1 in the previous year
start_dates = df['witer_year'].apply(lambda y: pd.Timestamp(year=y, month=11, day=1))
df['dow'] = (df['date'] - start_dates).dt.days


#print(df.head())
#print(df.tail())

# sed data for a Hovmöller diagram
hov_data = df.pivot(index='witer_year', columns='dow', values=' mean_ice_coverage [%]')


# create a figure
fig, ax = plt.subplots()

im = ax.imshow( hov_data.values,
    aspect='auto', origin='lower',
    cmap='YlGn', interpolation='none', extent=[
        hov_data.columns.min(), hov_data.columns.max(),
        hov_data.index.min(), hov_data.index.max()
    ]
)


# cosmetics
ticks_dow = np.linspace(hov_data.columns.min(), hov_data.columns.max(), 8, dtype=int)
tick_labels = [(pd.Timestamp('2000-11-01') + pd.Timedelta(days=int(d))).strftime('%b-%d')
               for d in ticks_dow]
ax.set_xticks(ticks_dow)
ax.set_xticklabels(tick_labels, rotation=45)
ax.set_yticks(np.arange(hov_data.index.min(), hov_data.index.max() + 1, 1))
ax.set_yticklabels(hov_data.index.astype(int))

ax.set_xlabel('Date')
ax.set_ylabel('Winer Year')

cbar = fig.colorbar(im, ax=ax, label='ice concentration [%]')

plt.savefig('duration.png',dpi=100)
#plt.show()



