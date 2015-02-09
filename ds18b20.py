import plotly.plotly as py
from w1thermsensor import W1ThermSensor
import json
import time
import datetime

with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 200
        }
    }], filename='Raspberry Pi Streaming Example Values')

print "View your streaming graph here: ", url

# temperature sensor middle pin connected channel 0 of mcp3008
sensor = W1ThermSensor()

stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

# the main sensor reading and plotting loop
while True:
    # temperature in celsius
    temp_C = sensor.get_temperature()
    # convert celsius to fahrenheit
    temp_F = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    # show only one decimal place for temperature
    temp_C = "%.1f" % temp_C
    temp_F = "%.1f" % temp_F

    # write the data to plotly
    stream.write({'x': datetime.datetime.now(), 'y': temp_C})

    # delay between stream posts
    time.sleep(0.25)
