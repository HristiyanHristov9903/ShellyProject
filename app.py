import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("✅ Connected to MQTT broker")
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(f"\n📌 Topic: {msg.topic}")

    payload = msg.payload.decode()

    try:
        data = json.loads(payload)

        if "params" in data:
            params = data["params"]

            if "switch:0" in params:
                switch = params["switch:0"]

                print("🔌 Switch:", "ON" if switch.get("output") else "OFF")

                if "apower" in switch:
                    print(f"⚡ Power: {switch['apower']} W")

                if "current" in switch:
                    print(f"🔋 Current: {switch['current']} A")

            if "temperature:0" in params:
                temp = params["temperature:0"]

                if "tC" in temp:
                    print(f"🌡 Temperature: {temp['tC']} °C")
    except:
        print(payload)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()