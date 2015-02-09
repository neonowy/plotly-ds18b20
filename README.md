# plotly-ds18b20
Simple sending temperature from DS18B20 sensor connected with Raspberry Pi to Plotly.

## Parts:

- Raspberry Pi
- Internet connection
- Dallas DS1B20 temperature sensor
- Hookup wires
- Breadboard
- Pi Cobbler or Adafruit Pi Shield

## Schematic:

Soon.

## Setup:

First install Python, dependencies etc.

```
sudo apt-get install python-dev
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python
sudo easy_install -U distribute
sudo apt-get install python-pip
sudo pip install rpi.gpio
sudo pip install plotly
sudo pip install w1thermsensor
git clone https://github.com/neonowy/plotly-ds18b20.git
```

Next copy your API key, streaming tokens and username to `config.json` file in `plotly-ds18b20` directory.

## Usage

```
cd plotly-ds18b20
sudo python ds18b20.py
```

That's all!

## Credits
Based on [Plotly example](https://plot.ly/raspberry-pi/tmp36-temperature-tutorial/).
