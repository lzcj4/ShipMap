import datetime
import json
from threading import Thread

import serial

from map.coordTransform_utils import wgs84_to_gcj02


class BDLocation:
    def __init__(self, **kwargs):
        self.id = ""
        self.time = kwargs["time"]
        self.lng = kwargs["lng"]
        self.lat = kwargs["lat"]
        self.height = kwargs["height"]

    def __str__(self):
        return "id:{0},time:{1},lng:{2},lat:{3},height:{4}".format(self.id, self.time, self.lng, self.lat, self.height)

    def to_json(self):
        return self.__dict__


class BDReceiver(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.current_id = None
        self.current_location = None

    def run(self):
        pass
        # self.read_serial()

    def read_serial(self):
        ser = serial.Serial(  # 下面这些参数根据情况修改
            port='COM5',
            baudrate=115200,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=5,
        )
        while ser.inWaiting() > 0:
            # read_bytes = ser.read(256)
            byte_line = ser.readline()
            if len(byte_line) > 0:
                str_len = str(byte_line, "utf-8")
                print(str_len)
                loc = self.parse(str_len)

    def parse(self, txt):
        id = self.get_id(txt)
        if id:
            self.current_id = id
            if self.current_location:
                self.current_location.id = id

        loc = self.get_location(txt)
        if loc:
            self.current_location = loc
            if self.current_id:
                self.current_location.id = self.current_id

        if self.current_id and self.current_location:
            result = self.current_location;
            self.current_id = None
            self.current_location = None
            return result
        else:
            return None

    def get_id(self, txt):
        if "$GPATT" not in txt:
            return None
        items = txt.split(',')
        id = items[9]
        return id

    def get_location(self, txt):
        if "$GNGGA" not in txt:
            return None
            # $GPGGA
            # 例：$GPGGA,092204.999,4250.5589,S,14718.5084,E,1,04,24.4,19.7,M,,,,0000*1F
            # 字段0：$GPGGA，语句ID，表明该语句为Global Positioning System Fix Data（GGA）GPS定位信息
            # 字段1：UTC 时间，hhmmss.sss，时分秒格式
            # 字段2：纬度ddmm.mmmm，度分格式（前导位数不足则补0）
            # 字段3：纬度N（北纬）或S（南纬）
            # 字段4：经度dddmm.mmmm，度分格式（前导位数不足则补0）
            # 字段5：经度E（东经）或W（西经）
            # 字段6：GPS状态，0=未定位，1=非差分定位，2=差分定位，3=无效PPS，6=正在估算
            # 字段7：正在使用的卫星数量（00 - 12）（前导位数不足则补0）
            # 字段8：HDOP水平精度因子（0.5 - 99.9）
            # 字段9：海拔高度（-9999.9 - 99999.9）
            # 字段10：地球椭球面相对大地水准面的高度
            # 字段11：差分时间（从最近一次接收到差分信号开始的秒数，如果不是差分定位将为空）
            # 字段12：差分站ID号0000 - 1023（前导位数不足则补0，如果不是差分定位将为空）
            # 字段13：校验值

        items = txt.split(',')
        local_time = self._get_time(items[1])
        wgs_lat = self._get_lat(items[2], items[3])
        wgs_lng = self._get_lng(items[4], items[5])
        status = int(items[6])
        satelites = int(items[7])
        height = float(items[9])
        gcj_lng, gcj_lat = wgs84_to_gcj02(wgs_lng, wgs_lat)
        loc = BDLocation(time=local_time, lng=gcj_lng, lat=gcj_lat, height=height)
        return loc

    def _get_time(self, time_str):
        dt = datetime.time(hour=int(time_str[0:2]), minute=int(time_str[2:4]), second=int(time_str[4:6]))
        return dt

    def _get_lng(self, lng_str, dir_str):
        lng = int(lng_str[0:3]) + float(lng_str[3:]) / 60
        return lng

    def _get_lat(self, lat_str, dir_str):
        lat = int(lat_str[0:2]) + float(lat_str[2:]) / 60
        return lat


if __name__ == "__main__":
    bd = BDReceiver()
    bd.start()

    txt = ("$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
           "$GNRMC,141450.00,A,3015.17726,N,11955.99100,E,0.48,5.610,021217,0.0,0,A*68",
           "$GNGGA,141450.00,3015.17726,N,11955.99100,E,1,03,16.4,81.30,M,6.700,M,0.00,0000*68"
           "$GNZDA,141450.00,02,12,2017,00,00*78")
    bs = b'\x41\x42\x43'
    s = str(bs, "utf-8")
    for item in txt:
        loc = bd.parse(item)
        if loc:
            print(loc)
