

from microWebSrv import MicroWebSrv

import json
import machine





def show_color(hexcolor):
    red = machine.PWM(machine.Pin(4))
    green = machine.PWM(machine.Pin(2))
    blue = machine.PWM(machine.Pin(18))
    red.freq(122)
    green.freq(122)
    blue.freq(122)
    h= hexcolor.lstrip('#')
    color_rgb = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    red.duty(color_rgb[0])
    green.duty(color_rgb[1])
    blue.duty(color_rgb[2])


def _httpHandlerAddColorPost(httpClient, httpResponse):
    with open('/www/colors.json') as colors_json:
        colors_raw = json.load(colors_json)
    all_colors_json = dict(**colors_raw['defaults'], **colors_raw['user_set'])
    content = httpClient.ReadRequestContent()
    content_json = json.loads(content)
    name,color = content_json['name'],content_json['color']
    if name in all_colors_json.keys():
        pass
        #send name already exists error
    if color in all_colors_json.values():
        pass
        #send color already exists with name error
    else:
        colors_raw['user_set'].update({name:color})
        with open('/www/colors.json','w') as colors_json:
            colors_json.write(json.dumps(colors_raw,indent=4))
        #send succesfull submit response

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
