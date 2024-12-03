import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

def connect_ethernet():
    # Initialize the Ethernet interface
    nic = network.LAN(mdc=Pin(23), mdio=Pin(18), power=Pin(12), phy_type=network.PHY_LAN8720, phy_addr=0)
    
    # Activate the interface
    nic.active(True)
    
    # Configure the interface (static IP in this case)
    nic.ifconfig(('192.168.13.2', '255.255.255.0', '192.168.13.1', '8.8.8.8'))
    
    # Wait for the connection to be established
    while not nic.isconnected():
        print("Connecting to Ethernet...")
        time.sleep(1)
        
    print("Ethernet connected!")
    print("IP address:", nic.ifconfig()[0])
    return nic

def check_connection(nic):
    if not nic.isconnected():
        print("Ethernet connection lost. Attempting to reconnect...")
        return connect_ethernet()
    return nic

# Callback function for when a message is received
def on_message(topic, msg):
    print(f"Received message '{msg.decode()}' on topic '{topic.decode()}'")

# MQTT configuration
brokerIP = "192.168.10.2"
brokerPort = 1883

myTopic = b"Optilogic/user/action"
client_id = b"ESP32_Client"

# Initial connection
nic = connect_ethernet()

# Initialize MQTT client
mqtt_client = MQTTClient(client_id, brokerIP, port=brokerPort)

# Set the callback function for receiving messages
mqtt_client.set_callback(on_message)

# Connect to the MQTT broker
try:
    mqtt_client.connect()
    print("Connected to MQTT Broker!")
    
    # Subscribe to the topic
    mqtt_client.subscribe(myTopic)

except Exception as e:
    print(f"Failed to connect to the MQTT broker: {e}")

# Main loop
while True:
    if nic:
        # Check Ethernet connection periodically
        nic = check_connection(nic)

        # Process incoming messages
        mqtt_client.check_msg()  # This will call the on_message callback when a message is received
        
        # Check connection periodically
        nic = check_connection(nic)
    else:
        print("No Ethernet connection. Attempting to reconnect...")
        nic = connect_ethernet()
    
    time.sleep(1)  # Wait for 10 seconds before next checkimport network
