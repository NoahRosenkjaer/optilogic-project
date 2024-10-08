import paho.mqtt.client as mqtt
import random

brokerIP        = "127.0.0.1"
brokerPort      = 1883
brokerKeepAlive = 60

myTopic   = "test"
myPayload = random.randint(0,99)
myQoS     = 1
myRetain  = True

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("user", "$7$101$yf94T8QG4zvJlcjM$EqNZNhFdEzWYU7WD3b1Eqj7XJ/qk6zSR1aqeYi8mf15o3vjuaBB5tVn8mLKJA3o+cwggfEW2atZm64X+fNGebg==")
client.connect(brokerIP, brokerPort, brokerKeepAlive)
client.publish(topic =  myTopic, qos = myQoS, payload = myPayload, retain = myRetain);

print(str(myPayload) + " has been published on broker " + brokerIP + ":" + str(brokerPort) + " on topic: " + myTopic  )
client.disconnect();
