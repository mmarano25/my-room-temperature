# my-room-temperature
Python and bash scripts for collecting temperature data from a pi, copying it to a home computer and graphing it.

## Overview

This program collects temperature sensor data from a remote Raspberry pi and 
graphs it. 

## Files

fetch_data_from_pi
    This is a bash script that ssh's into the pi using a private key and 
    uses rsync to download new data written from the temperature sensor.
    It then logs the successful or unsuccessful attempt to a log in /tmp.

graph_data.py
    This python script uses the library plotly to graph the temperature data.
    It turns the text file of data and temperatures into two lists of x and 
    y coordinates, then runs them through plotly's scatter graph utility.

temperature_sensor_code.py
    This python script, based initially off an online tutorial, reads the 
    temperature sensor located in /sys/bus/w1/devices/ and writes the result
    to a text file every minute. It uses python's built in datetime library 
    to log the time. 
    To keep this file running in the background, I used nohup and redirected
    the programs output to a nohup.out file not seen here. 


## Future Changes

I'd like to add the ability to choose a date range to display.
I'd also like to add more sensors to the Pi.
