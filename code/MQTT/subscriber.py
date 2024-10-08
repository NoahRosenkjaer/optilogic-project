import paho.mqtt.client as mqtt
import time

broker = '127.0.0.1'
topic = 'test'

# def get_info():
#     with open("C:\\Program files", 'r') as file:
#         line = file.readline()
#     print(line)


def on_connect(client, userdata, flags, rc, properties):
    print("Connected with result code " + str(rc))
    print(f"Subscriber til {topic}")

def on_publish(client, userdata, mid):
    print("Data published \n")


def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

print("connecting to broker")
client.connect(broker, port=1883)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.username_pw_set("admin", "$7$101$yf94T8QG4zvJlcjM$EqNZNhFdEzWYU7WD3b1Eqj7XJ/qk6zSR1aqeYi8mf15o3vjuaBB5tVn8mLKJA3o+cwggfEW2atZm64X+fNGebg==")
except:
    print("could not authenticate")

client.loop_start()
client.subscribe(topic)
while True:
    
    client.on_message
    time.sleep(5)