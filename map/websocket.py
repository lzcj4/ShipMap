import json

from channels import Group
from channels.message import Message

from map.RadarReceiver import RadarReceiver
from map.wshandler import add_or_update_area, get_all_area


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


WS_CMD = JSONObject({'connect': 0, 'area': 1, 'radar': 2})


def ws_connect(message: Message):
    Group("radar").add(message.reply_channel)
    print("ws_connect:{0}".format(message.content['client']))


def ws_send(txt):
    if txt:
        Group("radar").send({"text": txt}, immediately=True)


def ws_radar_lnglat(json_obj):
    if json_obj:
        js_msg = {'cmd': WS_CMD.radar, "msg": "get a new radar lnglat", 'json': json_obj}
        ws_send(json.dumps(js_msg))


def ws_message(message: Message):
    Group("radar").add(message.reply_channel)
    txt = message.content['text']
    print("ws_message:{0}".format(txt))
    txt_obj = json.loads(txt, object_hook=JSONObject)

    if txt_obj.cmd == WS_CMD.connect:
        areas = get_all_area()
        txt = {'cmd': WS_CMD.area, "msg": "get;{0} areas".format(len(areas)), 'json': areas}
        message.reply_channel.send({"text": json.dumps(txt)})
    elif txt_obj.cmd == WS_CMD.area:
        json_obj = json.loads(txt_obj.json, object_hook=JSONObject)
        add_or_update_area(json_obj)
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

    radar.set_callback(ws_radar_lnglat)
    radar.start_radar_receiver()
    is_radar_running = True


start_radar()
