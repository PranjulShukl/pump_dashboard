import json
import time
import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand
from my_app.models import Inverter1Data

# MQTT connection details
MQTT_BROKER = "216.10.247.180"
MQTT_PORT = 1883  # Default MQTT port
MQTT_TOPIC = "enigma/test"

class Command(BaseCommand):
    help = 'Run MQTT client to listen to sensor data'

    def handle(self, *args, **kwargs):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
                client.subscribe(MQTT_TOPIC)
            else:
                print(f"Failed to connect, return code {rc}")

        def on_message(client, userdata, msg):
            try:
                payload = json.loads(msg.payload.decode())
                data = {
                    'holding_reg1': payload.get('holding_reg1', 0.0),
                    'holding_reg2': payload.get('holding_reg2', 0.0),
                    'holding_reg3': payload.get('holding_reg3', 0.0),
                    'holding_reg4': payload.get('holding_reg4', 0.0),
                    'holding_reg5': payload.get('holding_reg5', 0.0),
                    'holding_reg6': payload.get('holding_reg6', 0.0),
                    'holding_reg7': payload.get('holding_reg7', 0.0),
                    'holding_reg8': payload.get('holding_reg8', 0.0),
                    'holding_reg9': payload.get('holding_reg9', 0.0),
                    'holding_reg10': payload.get('holding_reg10', 0.0),
                    'holding_reg11': payload.get('holding_reg11', 0.0),
                    'holding_reg12': payload.get('holding_reg12', 0.0),
                }
                Inverter1Data.objects.create(**data)
                print("Data updated:", data)
            except Exception as e:
                print("Exception occurred:", str(e))

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_forever()
