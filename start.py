from microWebSrv import MicroWebSrv

import json


def _httpHandlerLEDPost(httpClient, httpResponse):
    content = httpClient.ReadRequestContent()  # Read JSON color data
    colors = json.loads(content)
    print(colors)
    httpResponse.WriteResponseJSONOk()

routeHandlers = [ ( "/led-try", "POST",  _httpHandlerLEDPost ) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)
