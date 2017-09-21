import plotly as plt
import plotly.graph_objs as go


data_file = '/home/matt/pi_data/temperature.log'
dates = []
temps = []

with open( data_file, 'r' ) as f:
    for line in f:
        date =   ' '.join( line.split()[1:] )[1:-2] # second and third term, need to combine and join as a list then remove apostrophes and parenthese
        temp = line.split()[0][1:-1]              # first term, need to remove parenthese and comma
        dates.append( date )
        temps.append( temp )

trace = go.Scatter( 
        x = dates,
        y = temps,
)

plt.plotly.image.save_as( [trace], "temp_file.png" )
