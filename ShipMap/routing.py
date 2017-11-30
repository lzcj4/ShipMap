from channels import route

from map.websocket import ws_message, ws_disconnect, ws_connect

#    "websocket.connect": "com.lassoapp.consumers.websocket_connect",
#    "websocket.keepalive": "com.lassoapp.consumers.websocket_keepalive",
#    "websocket.disconnect": "com.lassoapp.consumers.websocket_disconnect"

channel_routing = [
    # route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect)]
