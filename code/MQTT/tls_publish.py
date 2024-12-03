import paho.mqtt.client as mqtt
import random
import ssl

brokerIP        = "pi"
brokerPort      = 8883
brokerKeepAlive = 60

myTopic   = "Optilogic/user/action"
myPayload = random.randint(0, 99)
myQoS     = 0
myRetain  = True

# Replace with your actual username and password
username = "rasmus"
password = "1234"

# Path to your CA certificate file
ca_cert = "/home/pi/Desktop/ca.crt"

# Create a new MQTT client instance
client = mqtt.Client()

# Set username and password for authentication
client.username_pw_set(username, password)

# Configure TLS/SSL
client.tls_set(ca_certs=ca_cert, tls_version=ssl.PROTOCOL_TLSv1_2)

# Disable hostname verification (use only for testing, not recommended for production)
#client.tls_insecure_set(True)

try:
    # Connect to the broker
    client.connect(brokerIP, brokerPort, brokerKeepAlive)

    # Publish the message
    result = client.publish(topic=myTopic, qos=myQoS, payload=myPayload, retain=myRetain)
    
    # Check if the message was published successfully
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"{myPayload} has been published on broker {brokerIP}:{brokerPort} on topic: {myTopic}")
    else:
        print(f"Failed to publish message. Return code: {result.rc}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Disconnect from the broker
    client.disconnect()