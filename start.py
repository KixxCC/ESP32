

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
    with open('./www/colors.json') as colors_json:
        colors_raw = json.load(colors_json)
    all_colors_json = colors_raw['defaults'].copy()
    all_colors_json.update(colors_raw['user_set'])
    print('si')
    content = httpClient.ReadRequestContent()
    print(content,'si')
    content_json = json.loads(content)
    name,color = content_json['name'],content_json['color']
    if name in all_colors_json.keys():
        color_name_exists = all_colors_json[name]
        httpResponse.WriteResponseJSONError(409, obj={"error":"Name already taken", "content":color_name_exists})
            #send name already exists error with color
    elif color in all_colors_json.values():
        color_name = all_colors_json.keys()[all_colors_json.values().index(color)]
        httpResponse.WriteResponseJSONError(409, obj={"error":"Color already exists", "content": color_name})
        #send color already exists error with name
    else:
        print('here')
        colors_raw['user_set'].update({name:color})
        with open('/www/colors.json','w') as colors_json:
            colors_json.write(json.dumps(colors_raw,indent=4))
        print('here')
        httpResponse.WriteResponseJSONOk()

def _httpHandlerColorTryPost(httpClient, httpResponse):
    content = httpClient.ReadRequestContent()  # Read JSON color data
    colors = json.loads(content)

    print(colors['color'])

    httpResponse.WriteResponseJSONOk()

routeHandlers = [ ( "/color-try", "POST",  _httpHandlerColorTryPost ),("/color-append", "POST", _httpHandlerAddColorPost) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)
show_color('#ffffff')
