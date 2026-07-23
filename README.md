# Shelly MQTT Dashboard

A Python application for monitoring Shelly smart devices using MQTT.

## Project Description

This project demonstrates how to collect real-time data from Shelly smart devices using the MQTT protocol and display it in a terminal dashboard.

The application receives data from:

- Shelly Plug S Gen3
- Shelly BLU H&T
- Shelly BLU Door/Window

## Features

- Real-time MQTT communication
- Displays plug state (ON/OFF)
- Displays power consumption
- Displays voltage and current
- Displays plug temperature
- Displays BLU H&T temperature, humidity and battery
- Displays BLU Door/Window status, angle, light level, RSSI and battery

## Technologies

- Python 3
- Paho MQTT
- Mosquitto MQTT Broker
- Shelly Smart Devices

## MQTT Topics

### Shelly Plug S Gen3

- `.../status/switch:0`
- `.../events/rpc`

### Shelly BLU H&T

- `shelly/blu/ht/temperature`
- `shelly/blu/ht/humidity`
- `shelly/blu/ht/battery`

### Shelly BLU Door/Window

The application reads Door/Window events from the Shelly RPC event stream and displays:

- Open/Closed status
- Rotation angle
- Illuminance
- RSSI
- Battery level

## Installation

Clone the repository:

```bash
git clone https://github.com/HristiyanHristov9903/ShellyProject.git
```

Install dependencies:

```bash
pip install paho-mqtt
```

Start Mosquitto:

```bash
brew services start mosquitto
```

Run the application:

```bash
python app.py
```

## Author

Hristiyan Hristov