from channels.auth import channel_session_user_from_http
from channels.handler import AsgiHandler
from django.http import HttpResponse
from channels.message import Message

from map.RadarReceiver import RadarReceiver, client_cache

is_radar_running = False
radar = RadarReceiver()


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


def start_radar():
    global is_radar_running, radar
    if is_radar_running:
        return
    radar.start_radar_receiver()
    is_radar_running = True

@channel_session_user_from_http
def ws_message(message: Message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    client_cache.append(message.reply_channel)
    print("ws in :{0}".format(message.content['text']))
    message.reply_channel.send({
        "text": "Server reply",
    })


def ws_disconnect(message: Message):
    client_cache.remove(message)


start_radar()
