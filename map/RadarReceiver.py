import json
import random
import socket
import threading

from ctypes import (
    Structure, Union, Array,
    c_float, c_byte
)

from ShipMap import settings


class uint8_array(Array):
    _type_ = c_byte
    _length_ = 4


class C_ReadUnion(Union):
    _fields_ = ("data", c_float), ("chunk", uint8_array)


class C_ReadUnion_8(Array):
    _type_ = C_ReadUnion
    _length_ = 8


class C_Location(Structure):
    _fields_ = ("latitude", C_ReadUnion), ("longitude", C_ReadUnion), ("altitude", C_ReadUnion), \
               ("distance", C_ReadUnion), ("orientation", C_ReadUnion), ("height", C_ReadUnion), \
               ("speed", C_ReadUnion), ("direction", C_ReadUnion), ("reserve", C_ReadUnion_8)


class Location(object):
    def __init__(self, c_loc):
        if settings.DEBUG:
            self.latitude = round(c_loc.latitude.data, 5) + random.random()
            self.longitude = round(c_loc.longitude.data, 5) + random.random()
        else:
            self.latitude = round(c_loc.latitude.data, 5)
            self.longitude = round(c_loc.longitude.data, 5)
        self.altitude = round(c_loc.altitude.data, 2)
        self.distance = round(c_loc.distance.data, 2)
        self.orientation = round(c_loc.orientation.data, 2)
        self.height = round(c_loc.height.data, 2)
        self.speed = round(c_loc.speed.data, 2)
        self.direction = round(c_loc.direction.data, 2)

    def __str__(self):
        return "经度:{0},纬度:{1},海拔:{2},距离:{3},方位:{4},高度:{5},速度:{6},方向:{7}".format(
            self.longitude, self.latitude, self.altitude, self.distance,
            self.orientation, self.height, self.speed, self.direction)

    def to_json(self):
        js = json.dumps(self.__dict__)
        return js


HOST = '127.0.0.1'
PORT = 8008

client_cache = []


class RadarReceiver:
    BUF_SIZE = 1024
    MAX_CONNECTIONS = 5
    DATA_LEN = 64

    def __init__(self, host=HOST, port=PORT):
        self.is_radar_running = True
        self.thread_radar = None
        self.host = host
        self.port = port
        self.items = []

    def get_items(self):
        return self.items

    def start_radar_receiver(self):
        """
        开启雷达接收线程
        :return:
        """
        self.is_radar_running = True
        self.thread_radar = threading.Thread(group=None, target=self.__start_socket_receiver)
        self.thread_radar.name = "RadarReceiver_Thread"
        self.thread_radar.start()

    def stop_radar_receiver(self):
        self.is_radar_running = False
        self.thread_radar.join()

    def __start_socket_receiver(self):
        server_addr = (self.host, self.port)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(server_addr)
        server.listen(RadarReceiver.MAX_CONNECTIONS)

        while self.is_radar_running:
            client, client_addr = server.accept()
            print('Connected by:%s', client_addr)
            while self.is_radar_running:
                read_bytes = client.recv(RadarReceiver.BUF_SIZE)
                if len(read_bytes) == 0:
                    break
                self.__parse_location(read_bytes)
        server.close()

    def __parse_location(self, data):
        index = 0
        # 4字节协议头，4字节数据条数
        header = data[index:index + 4]
        if header != b'\xaa\xaa\xaa\xaa':
            return

        index += 4
        ri = C_ReadUnion()
        ri.chunk[:] = data[index:index + 4]
        index += 4

        data_len = int(ri.data)
        self.host = "aaaa"
        for i in range(data_len):
            data_item = data[index:index + RadarReceiver.DATA_LEN]
            if len(data_item) != RadarReceiver.DATA_LEN:
                break
            index += RadarReceiver.DATA_LEN

            loc = C_Location()
            loc.latitude.chunk[:] = data_item[0 * 4: 1 * 4]
            loc.longitude.chunk[:] = data_item[1 * 4: 2 * 4]
            loc.altitude.chunk[:] = data_item[2 * 4: 3 * 4]

            loc.distance.chunk[:] = data_item[3 * 4: 4 * 4]
            loc.orientation.chunk[:] = data_item[4 * 4: 5 * 4]
            loc.height.chunk[:] = data_item[5 * 4: 6 * 4]
            loc.speed.chunk[:] = data_item[6 * 4: 7 * 4]

            loc.direction.chunk[:] = data_item[7 * 4: 8 * 4]

            l = Location(loc)
            for client in client_cache:
                client.send({"text": l.to_json()})
            print("- - {0}、{1};{2}".format(i, l, l.to_json()))
