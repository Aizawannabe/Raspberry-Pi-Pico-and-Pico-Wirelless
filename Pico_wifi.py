import network

# create a WiFi interface
wlan = network.WLAN(network.STA_IF)

# enable the WiFi interface
wlan.active(True)
# scan for available networks
networks = wlan.scan()

# print the list of networks
for network in networks:
    print(network[0])
# connect to a wireless network
wlan.connect("GEARBOX GUEST")
# check if connected to a wireless network
while not wlan.isconnected():
    pass

# print the IP address
print(wlan.ifconfig())

