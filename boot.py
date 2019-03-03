import network

def connect():
    password = "42971622156631733279"
    ssid = "Unserwlan"
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        return
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass
    print("Connection successful")
    print(station.ifconfig())
    station.config(dhcp_hostname='halloclara')
    print(station.config('dhcp_hostname'))

connect()
