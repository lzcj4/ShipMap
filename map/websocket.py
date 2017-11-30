import json

from channels import Group
from channels.message import Message

from map.RadarReceiver import RadarReceiver
from map.wshandler import add_or_update_area, get_all_areas


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


WS_CMD = JSONObject({'connect': 0, 'area': 1})


def ws_connect(message: Message):
    Group("radar").add(message.reply_channel)
    print("ws_connect:{0}".format(message.content['client']))


def ws_message(message: Message):
    Group("radar").add(message.reply_channel)
    txt = message.content['text']
    print("ws_message:{0}".format(txt))
    txt_obj = json.loads(txt, object_hook=JSONObject)

    if txt_obj.cmd == WS_CMD.connect:
        js_items = get_all_areas()
        js = {'cmd': WS_CMD.area, "msg": "return areas infos", 'json': js_items}
        message.reply_channel.send({"text": json.dumps(js)})
    elif txt_obj.cmd == WS_CMD.area:
        jsonObj = json.loads(txt_obj.json, object_hook=JSONObject)
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
