import network
import time
from umqtt.simple import MQTTClient
import ssl

# Wi-Fi credentials
SSID = "Phone_1_2058"
PASSWORD = "dhcp1234"

# MQTT Broker settings
BROKER_IP = "pi"
BROKER_PORT = 8883
BROKER_KEEPALIVE = 60

MY_TOPIC = b"Plant1/temperature"

# Replace with your actual username and password
USERNAME = b"rasmus"
PASSWORD = b"1234"

# CA certificate content (replace with your actual CA certificate)
CA_CERT = """
-----BEGIN CERTIFICATE-----
MIIDqzCCApOgAwIBAgIUBKCHRLFJ1EcU98oz7IekQc6b+10wDQYJKoZIhvcNAQEL
BQAwZTELMAkGA1UEBhMCREsxDDAKBgNVBAgMA0Z5bjEPMA0GA1UEBwwGT2RlbnNl
MQwwCgYDVQQKDANVQ0wxCzAJBgNVBAMMAnBpMRwwGgYJKoZIhvcNAQkBFg1wb2Vs
c2VAYXNkLmRrMB4XDTI0MTAyODA4NTI1OVoXDTI5MTAyODA4NTI1OVowZTELMAkG
A1UEBhMCREsxDDAKBgNVBAgMA0Z5bjEPMA0GA1UEBwwGT2RlbnNlMQwwCgYDVQQK
DANVQ0wxCzAJBgNVBAMMAnBpMRwwGgYJKoZIhvcNAQkBFg1wb2Vsc2VAYXNkLmRr
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmiDg0SbZWGgJKSfYPEL1
p0Meclp7Dt+QmYXGLItXjsgFwSI/ooIMU8QYm+cGbxuifpVcDJ1c147g7GbHOl/8
RG0tljJ80XllBZ8DZiVjy1xnZp5VOWRw4n/ooi5YAhVIh1wNvzeaZSkLnXfue3Wu
6//0+h+qhE/Z5tDL+kG/Pcx/4vRtxF3RemX77qyocq62uf/8NARBUfeWUzTeu1XD
Vv94R3uu6FlUrZZ0ZeEKmJ79Ot6lydrsKOT9E3vishVUgq8ohmRnLqZl501pBn3p
42IJeE53tVQZmcuO/Tcz7cFq7nZz3N81ilbJXbof+X6LnPe76KCnmeWF13t5Sjpa
8QIDAQABo1MwUTAdBgNVHQ4EFgQUH4mvZuTN+/Zdt4IVJZ2bkJLgtjIwHwYDVR0j
BBgwFoAUH4mvZuTN+/Zdt4IVJZ2bkJLgtjIwDwYDVR0TAQH/BAUwAwEB/zANBgkq
hkiG9w0BAQsFAAOCAQEASYnO3XgsEukl+NzajtfVsYIdKz9BiwHNm8oD+WJpcoqR
Gb4mR4WNMjJOXJUdbfR+w+pGP6b1SPzBpvWybxkKZkJtfW3wlBc6KHGnGabmNXhA
gcV7LEfP3GDUaTGA744Xe3eqoCoxN0E/JOQN/mtsmCXfBsPq8pSZKcYx8V7OREgv
79ZZ+DM57NMoCOl281FK1Zb8yOyh4qjHKn6YswQJZ9oAJDzXm8jOTUCMN00tbJ0Z
oeIeDMMcgBYukeeAnIkdqVhQ8DkqeJzsI5tudMWWFV3tiXsWl5REYu31oB5Eag7M
Ehd1+NUE+SgvVlpeM/HPqE04GOYsUI8X+W85NeufmA==
-----END CERTIFICATE-----
"""

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print("Connected to WiFi")
    print("IP address:", wlan.ifconfig()[0])

def on_message(topic, msg):
    print(f"Received message '{msg.decode()}' on topic '{topic.decode()}'")

def main():
    connect_wifi()
    
    client = MQTTClient("esp32-client", BROKER_IP, BROKER_PORT, USERNAME, PASSWORD, keepalive=BROKER_KEEPALIVE, ssl=True, ssl_params={'cert_reqs':ssl.CERT_REQUIRED, 'cadata':CA_CERT})
    
    client.set_callback(on_message)
    
    try:
        client.connect()
        print("Connected to MQTT Broker!")
        client.subscribe(MY_TOPIC)
        print(f"Subscribed to {MY_TOPIC}")
        
        while True:
            client.check_msg()
            time.sleep(1)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()