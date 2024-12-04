import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

def connect_ethernet():
    # Initialisering
    nic = network.LAN(mdc=Pin(23), mdio=Pin(18), power=Pin(12), phy_type=network.PHY_LAN8720, phy_addr=0)
    
    # Aktiverer interfacet
    nic.active(True)
    
    # Statisk konfiguration
    nic.ifconfig(('192.168.12.2', '255.255.255.0', '192.168.12.1', '8.8.8.8'))
    
    while not nic.isconnected():
        print("Forbinder til Ethernet...")
        time.sleep(1)
        
    print("Ethernet forbundet!")
    print("IP address:", nic.ifconfig()[0])
    return nic

def check_connection(nic):
    if not nic.isconnected():
        print("Ingen internet, Genforbinder")
        return connect_ethernet()
    return nic

# Callback function for when a message is received
def on_message(topic, msg):
    print(f"Besked: '{msg.decode()}' på topic '{topic.decode()}'")
    if msg == b'turn_on':
        print("Tænd for varmepumpekode")
        led.on()
    elif msg == b'turn_off':
        print("Sluk varmepumpe")
        led.off()

# MQTT configuration
brokerIP = "192.168.11.2"
brokerPort = 1883
mqtt_user = "rasmus"
mqtt_password = "1234"

myTopic = b"Optilogic/user/action"
client_id = b"ESP32_Client"

led = Pin(0, Pin.OUT)


nic = connect_ethernet()

# Initialiser MQTT client
mqtt_client = MQTTClient(client_id, brokerIP, port=brokerPort, user=mqtt_user, password=mqtt_password)

# Callback funktion
mqtt_client.set_callback(on_message)

# Connect til MQTT Broker
try:
    mqtt_client.connect()
    print("Connected to MQTT Broker!")
    
    # Subscribe to the topic
    mqtt_client.subscribe(myTopic)

except Exception as e:
    print(f"Failed to connect to the MQTT broker: {e}")

print("VARMEPUMPE = SLUKKET")
# Main loop
while True:
    if nic.isconnected():
        try:
            mqtt_client.check_msg()
        except Exception as e:
            print(f"Error checking messages: {e}")
            # Attempt to reconnect
            try:
                mqtt_client.connect()
            except:
                print("Failed to reconnect to MQTT broker")

    else:
        print("Ingen internetforbindelse, forbinder...")
        print("VARMEPUMPE = STANDARD MODE")
        try:
            nic = connect_ethernet()
            if nic.isconnected():
                mqtt_client.connect()
                print("Forbundet til broker")
                mqtt_client.subscribe(myTopic)
                print("Subscriber")
        except Exception as e:
            print(f"Failed to connect to the MQTT broker: {e}")
        time.sleep(2)
