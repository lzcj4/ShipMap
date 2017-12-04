import json

from channels import Group
from channels.message import Message

from map.RadarReceiver import RadarReceiver
from map.templates.BDReceiver import BDReceiver
from map.wshandler import add_or_update_area, get_all_area, remove_area


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


WS_CMD = JSONObject({'connect': 0, 'area': 1, 'radar': 2, 'area_delete': 3, 'beidou': 4})


def ws_connect(message: Message):
    """该回调不能用，导致WS连接挂掉，CHROME崩"""
    Group("radar").add(message.reply_channel)
    print("ws_connect:{0}".format(message.content['client']))


def ws_send(txt):
    if txt:
        Group("radar").send({"text": txt}, immediately=True)


def ws_send_radar_lnglat(json_obj):
    """
    发送雷达定位数据
    :param json_obj:
    :return:
    """
    if json_obj:
        js_msg = {'cmd': WS_CMD.radar, "msg": "get a new radar lnglat", 'json': json_obj}
        ws_send(json.dumps(js_msg))


def ws_send_bd_lnglat(json_obj):
    """
    发送北半定位数据
    :param json_obj:
    :return:
    """
    if json_obj:
        js_msg = {'cmd': WS_CMD.beidou, "msg": "get a new bd lnglat", 'json': json_obj}
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
    elif txt_obj.cmd == WS_CMD.area_delete:
        json_obj = json.loads(txt_obj.json, object_hook=JSONObject)
        remove_area(json_obj)
    else:
        pass


def ws_disconnect(message: Message):
    print("ws_disconnect")
    Group("radar").discard(message.reply_channel)


is_radar_running = False
radar_receiver = RadarReceiver()
bd_receiver = BDReceiver()


def start_receiver():
    global is_radar_running, radar_receiver
    if is_radar_running:
        return

    bd_receiver.set_callback(ws_send_bd_lnglat)
    bd_receiver.start()

    radar_receiver.set_callback(ws_send_radar_lnglat)
    radar_receiver.start_radar_receiver()
    is_radar_running = True


start_receiver()
