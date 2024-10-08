import paho.mqtt.client as mqtt
import random

brokerIP        = "localhost"
brokerPort      = 1883
brokerKeepAlive = 60

myTopic   = "Plant1/temperature"
myPayload = random.randint(0, 99)
myQoS     = 0
myRetain  = True

# Replace with your actual username and password
username = "rasmus"
password = "1234"

client = mqtt.Client()

# Set username and password for authentication
client.username_pw_set(username, password)

# Connect to the broker
client.connect(brokerIP, brokerPort, brokerKeepAlive)

# Publish the message
client.publish(topic=myTopic, qos=myQoS, payload=myPayload, retain=myRetain)

print(f"{myPayload} has been published on broker {brokerIP}:{brokerPort} on topic: {myTopic}")

# Disconnect from the broker
client.disconnect()