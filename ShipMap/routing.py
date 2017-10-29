from channels import route

from map.ws import ws_message

channel_routing = [route("websocket.receive", ws_message), ]
