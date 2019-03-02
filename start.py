from microWebSrv import MicroWebSrv

import json
import machine


red = machine.PWM(machine.Pin(4))
green = machine.PWM(machine.Pin(2))
blue = machine.PWM(machine.Pin(18))
red.freq(122)
green.freq(122)
blue.freq(122)


def show_color(hexcolor):
    h= hexcolor.lstrip('#')
    color_rgb = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    red.duty(color_rgb[0])
    green.duty(color_rgb[1])
    blue.duty(color_rgb[2])


def _httpHandlerAddColorPost(httpClient, httpResponse):
    content = httpClient.ReadRequestContent()
    color = json.loads(content)

def _httpHandlerLEDTryPost(httpClient, httpResponse):
    print("got somenthing")
    content = httpClient.ReadRequestContent()  # Read JSON color data
    colors = json.loads(content)
    show_color(colors['color'])
    httpResponse.WriteResponseJSONOk()

routeHandlers = [ ( "/color-try", "POST",  _httpHandlerLEDTryPost ) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)
show_color('#ffffff')
