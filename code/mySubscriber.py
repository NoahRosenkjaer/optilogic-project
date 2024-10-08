import paho.mqtt.client as mqtt

brokerIP        = "localhost"
brokerPort      = 1883
brokerKeepAlive = 60
myTopic         = "Plant1/temperature"

# Replace with your actual username and password
username = "rasmus"
password = "1234"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(myTopic)

def on_message(client, userdata, msg):
    print("Fetched: " + str(msg.payload.decode()) + " from topic " + msg.topic)

client = mqtt.Client()

# Set username and password for authentication
client.username_pw_set(username, password)

client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message    # Define callback function for receipt of a message

client.connect(brokerIP, brokerPort, brokerKeepAlive)

# Start the loop to process incoming messages continuously
client.loop_forever()