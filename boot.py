import network

def connect():
    password = "9261274132264035"
    ssid = "WLAN-QNAKN3"
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
