

from microWebSrv import MicroWebSrv
import json
import machine
red = machine.PWM(machine.Pin(18))
green = machine.PWM(machine.Pin(4))
blue = machine.PWM(machine.Pin(2))
red.freq(122)
green.freq(122)
blue.freq(122)

def show_color(color):
    global red
    global blue
    global green
    color_rgb = color.split(',')
    red.duty(int(color_rgb[0]))
    green.duty(int(color_rgb[1]))
    blue.duty(int(color_rgb[2]))

def _httpHandlerJsoncolorRequest(httpClient, httpResponse):
    httpResponse.WriteResponseFile('/JSON-files/colors.json', contentType='application/json', headers=None)

def _httpHandlerAddColorPost(httpClient, httpResponse):
    with open('/JSON-files/colors.json') as colors_json:
        colors_raw = json.load(colors_json)
    all_colors_json = colors_raw['defaults'].copy()
    all_colors_json.update(colors_raw['user_set'])
    content = httpClient.ReadRequestContent()
    content_json = json.loads(content)
    name,color = content_json['name'],content_json['color']
    print('here')
    if name in all_colors_json.keys():
        color_name_exists = all_colors_json[name]
        httpResponse.WriteResponseJSONError(409, obj={"error":"Name already taken", "content":color_name_exists})
            #send name already exists error with color
    elif color in all_colors_json.values():
        color_name = all_colors_json.keys()[all_colors_json.values().index(color)]
        httpResponse.WriteResponseJSONError(409, obj={"error":"Color already exists", "content": color_name})
        #send color already exists error with name
    else:
        colors_raw['user_set'].update({name:color})
        with open('/JSON-files/colors.json','w') as colors_json:
            json.dump(colors_raw,colors_json)
        httpResponse.WriteResponseJSONOk()
        with open('/JSON-files/colors.json') as colors_json:
            print(json.load(colors_json))

def _httpHandlerColorTryPost(httpClient, httpResponse):
    content = httpClient.ReadRequestContent()  # Read JSON color data
    colors = json.loads(content)
    show_color(colors['color'])
    httpResponse.WriteResponseJSONOk()


routeHandlers = [ ( "/color-try", "POST",  _httpHandlerColorTryPost ),("/color-append", "POST", _httpHandlerAddColorPost),("/colors-json", "GET", _httpHandlerJsoncolorRequest) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)
