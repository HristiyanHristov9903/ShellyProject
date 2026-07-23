# Shelly MQTT Client

A Python application that connects to a Mosquitto MQTT broker and receives telemetry data from a Shelly Plug S Gen3 using MQTT.

## Features

- Connects to a local MQTT broker
- Receives MQTT messages from Shelly Plug S Gen3
- Displays:
  - Switch state (ON/OFF)
  - Power (W)
  - Current (A)
  - Temperature (°C)

## Requirements

- Python 3
- Mosquitto MQTT Broker
- paho-mqtt

## Installation

```bash
pip3 install -r requirements.txt
```

## Run

```bash
python3 app.py
```