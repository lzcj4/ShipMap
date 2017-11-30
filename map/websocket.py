import json

from channels import Group
from channels.message import Message

from map.RadarReceiver import RadarReceiver
from map.wshandler import add_or_update_area


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


WS_CMD = JSONObject({'test': -1, 'area': 0})


def ws_connect(message: Message):
    Group("radar").add(message.reply_channel)
    print("ws_connect:{0}".format(message.content['client']))


def ws_message(message: Message):
    Group("radar").add(message.reply_channel)
    txt = message.content['text']
    print("ws_message:{0}".format(txt))
    txt_obj = json.loads(txt, object_hook=JSONObject)
    if txt_obj.json != "":
        jsonObj = json.loads(txt_obj.json, object_hook=JSONObject)
        if txt_obj.cmd == WS_CMD.test:
            pass
        elif txt_obj.cmd == WS_CMD.area:
            add_or_update_area(jsonObj)
        else:
            pass


def ws_disconnect(message: Message):
    print("ws_disconnect")
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
