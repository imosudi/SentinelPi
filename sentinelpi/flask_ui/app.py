from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt
import os

app = Flask(__name__)

# Load configuration from environment variables
app.config['MQTT_BROKER'] = os.getenv('MQTT_BROKER', 'localhost')
app.config['MQTT_PORT'] = int(os.getenv('MQTT_PORT', 1883))
app.config['MQTT_TOPIC'] = os.getenv('MQTT_TOPIC', 'home/surveillance')

# MQTT client setup
mqtt_client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code: " + str(rc))
    client.subscribe(app.config['MQTT_TOPIC'])

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(app.config['MQTT_BROKER'], app.config['MQTT_PORT'], 60)
mqtt_client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/alerts', methods=['POST'])
def alerts():
    data = request.json
    # Process the alert data (e.g., send to Telegram, log, etc.)
    print(f"Alert received: {data}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('path/to/cert.pem', 'path/to/key.pem'))