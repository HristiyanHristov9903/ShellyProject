import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

plug = {
    "state": "Unknown",
    "power": 0,
    "voltage": 0,
    "current": 0,
    "temperature": 0,
}

blu = {
    "temperature": 0,
    "humidity": 0,
    "battery": 0,
}


def print_dashboard():
    print("\033[2J\033[H", end="")  # Clear terminal

    print("╔══════════════════════════════════════════════╗")
    print("║          SHELLY MQTT DASHBOARD              ║")
    print("╚══════════════════════════════════════════════╝")

    print("\n🔌 SHELLY PLUG S GEN3")
    print("──────────────────────────────────────────────")
    print(f"State        : {plug['state']}")
    print(f"⚡ Power      : {plug['power']} W")
    print(f"🔋 Voltage    : {plug['voltage']} V")
    print(f"🔄 Current    : {plug['current']} A")
    print(f"🌡️ Temperature: {plug['temperature']} °C")

    print("\n🌡️ SHELLY BLU H&T")
    print("──────────────────────────────────────────────")
    print(f"🌡️ Temperature: {blu['temperature']} °C")
    print(f"💧 Humidity   : {blu['humidity']} %")
    print(f"🔋 Battery    : {blu['battery']} %")

    print("\n══════════════════════════════════════════════")


def on_connect(client, userdata, flags, reason_code, properties=None):
    print("✅ Connected to MQTT broker\n")
    client.subscribe("#")


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    # -------- BLU H&T --------

    if topic == "shelly/blu/ht/temperature":
        blu["temperature"] = payload
        print_dashboard()
        return

    if topic == "shelly/blu/ht/humidity":
        blu["humidity"] = payload
        print_dashboard()
        return

    if topic == "shelly/blu/ht/battery":
        blu["battery"] = payload
        print_dashboard()
        return

    # -------- Shelly Plug --------

    try:
        data = json.loads(payload)
    except:
        return

    if topic.endswith("/status/switch:0"):

        plug["state"] = "ON" if data.get("output") else "OFF"
        plug["power"] = data.get("apower", 0)
        plug["voltage"] = data.get("voltage", 0)
        plug["current"] = data.get("current", 0)

        if "temperature" in data:
            plug["temperature"] = data["temperature"].get("tC", 0)

        print_dashboard()

    elif topic.endswith("/events/rpc"):

        params = data.get("params", {})

        sw = params.get("switch:0")

        if sw:
            plug["state"] = "ON" if sw.get("output") else "OFF"
            plug["power"] = sw.get("apower", plug["power"])
            plug["voltage"] = sw.get("voltage", plug["voltage"])
            plug["current"] = sw.get("current", plug["current"])

        temp = params.get("temperature:0")

        if temp:
            plug["temperature"] = temp.get("tC", plug["temperature"])

        print_dashboard()


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_forever()