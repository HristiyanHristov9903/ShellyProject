# Shelly MQTT Monitoring System

## Overview

This project demonstrates an IoT monitoring system using MQTT and Shelly devices.

## Hardware

- Shelly Plug S Gen3
- Shelly BLU H&T
- MacBook Air
- Mosquitto MQTT Broker

## Software

- Python 3
- paho-mqtt
- Mosquitto
- Git

## Features

- Real-time power monitoring
- Voltage monitoring
- Current monitoring
- Plug temperature monitoring
- Ambient temperature monitoring
- Humidity monitoring
- Battery level monitoring
- MQTT communication
- Live terminal dashboard

## MQTT Topics

```
shelly/blu/ht
shelly/blu/ht/temperature
shelly/blu/ht/humidity
shelly/blu/ht/battery
```

## Run

```bash
python3 app.py
```

## Author

Hristiyan Hristov