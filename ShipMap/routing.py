from channels import route

from map.ws import ws_message, ws_disconnect
#    "websocket.connect": "com.lassoapp.consumers.websocket_connect",
#    "websocket.keepalive": "com.lassoapp.consumers.websocket_keepalive",
#    "websocket.disconnect": "com.lassoapp.consumers.websocket_disconnect"

channel_routing = [route("websocket.receive", ws_message), route("websocket.disconnect", ws_disconnect)]
