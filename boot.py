import network

def connect():
    password = ""
    ssid = ""
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
    station.config( dhcp_hostname='tardis')
    print(station.config('dhcp_hostname'))

connect()
