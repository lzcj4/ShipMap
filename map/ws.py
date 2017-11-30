from channels import Group
from channels.message import Message

from map.RadarReceiver import RadarReceiver

def ws_message(message: Message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    Group("radar").add(message.reply_channel)
    print("ws in :{0}".format(message.content['text']))
    # message.reply_channel.send({
    #     "text": "Server reply",
    # })


def ws_disconnect(message: Message):
    Group("radar").discard(message.reply_channel)


is_radar_running = False
radar = RadarReceiver()


def start_radar():
    global is_radar_running, radar
    if is_radar_running:
        return
    radar.start_radar_receiver()
    is_radar_running = True


start_radar()
