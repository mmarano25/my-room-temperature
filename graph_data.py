#!/usr/bin/env python3

import plotly as plt
import plotly.graph_objs as go
from datetime import datetime


data_file = '/home/matt/pi_data/temperature.log'
dates = []
temps = []
dates_to_graph = []
temps_to_graph = []

try:
    with open( data_file, 'r' ) as f:
        for line in f:
            date =   ' '.join( line.split()[1:] )[1:-2] # second and third term, need to combine and join as a list then remove apostrophes and parenthese
            temp = line.split()[0][1:-1]              # first term, need to remove parenthese and comma
            dates.append( date )
            temps.append( temp )
except OSError:
    print( "Error occurred opening and reading ", data_file )


first_day  = datetime.strptime( dates[0], "%Y-%m-%d %H:%M:%S" )
print( first_day )
date_range = max_date_range = (datetime.now() - first_day).days

user_date_range = int( input( "How many days back do you want to see?\n" ) )
if( user_date_range > max_date_range ):
    print( "Sorry, only data from the past {} days is available.".format(date_range) )
else:
    date_range = int(user_date_range)

for n in range(len(dates)-1,-1,-1):
    current_date = datetime.strptime( dates[n], "%Y-%m-%d %H:%M:%S" )
    diff = (datetime.now()-current_date).days
    if( diff > date_range ):
        dates_to_graph = dates[n:]
        temps_to_graph = temps[n:]
        break

trace = go.Scatter( 
        x = dates_to_graph,
        y = temps_to_graph,
)
plt.plotly.image.save_as( [trace], "temp_file.png" )

