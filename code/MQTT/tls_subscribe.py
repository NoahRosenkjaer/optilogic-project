import paho.mqtt.client as mqtt
import ssl

brokerIP        = "pi"
brokerPort      = 8883
brokerKeepAlive = 60

myTopic   = "Optilogic/user/action"

# Replace with your actual username and password
username = "rasmus"
password = "1234"

# Path to your CA certificate file
ca_cert = "/home/pi/Desktop/ca.crt"

# Callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

# Callback function for when the client connects
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        # Subscribe to the topic
        client.subscribe(myTopic)
    else:
        print(f"Failed to connect, return code {rc}")

# Create a new MQTT client instance
client = mqtt.Client()

# Set username and password for authentication
client.username_pw_set(username, password)

# Configure TLS/SSL
client.tls_set(ca_certs=ca_cert, tls_version=ssl.PROTOCOL_TLSv1_2)

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

try:
    # Connect to the broker
    client.connect(brokerIP, brokerPort, brokerKeepAlive)

    # Start the loop to process received messages
    client.loop_forever()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Disconnect from the broker
    client.disconnect()