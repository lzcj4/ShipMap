import datetime
from threading import Thread
import time

import serial

from map.geoutil import wgs84_to_gcj02
from map.models import Ship


class BDLocation:
    def __init__(self, **kwargs):
        self.id = ""
        self.time = str(kwargs["time"])
        self.lng = kwargs["lng"]
        self.lat = kwargs["lat"]
        self.height = kwargs["height"]

    def __str__(self):
        return "id:{0},time:{1},lng:{2},lat:{3},height:{4}".format(self.id, self.time, self.lng, self.lat, self.height)

    def to_json(self):
        ships = Ship.objects.filter(no=self.id)
        result = self.__dict__
        if ships:
            ship = ships[0]
            result["name"] = ship.name
            result["harbor"] = ship.harbor
            result["caption"] = ship.caption
            result["phone"] = ship.phone
            result["address"] = ship.address

        return result


READ_COM = "COM5"


class BDReceiver(Thread):
    """
    北斗数据接收器
    """

    def __init__(self):
        Thread.__init__(self)
        self.name = "BDReceiver_thread_1"
        self.is_running = True
        self.current_id = None
        self.current_location = None
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def run(self):
        self.is_running = True
        self.mock_run()
        # self.read_serial()

    def stop(self):
        self.is_running = False

    def mock_run(self):
        time.sleep(10)
        msgs = ("$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141450.00,A,3015.17726,N,11955.99100,E,0.48,5.610,021217,0.0,0,A*68                 ",
                "$GNGGA,141450.00,3015.17726,N,11956.99100,E,1,03,16.4,81.30,M,6.700,M,0.00,0000*68         ",
                "$GNZDA,141450.00,02,12,2017,00,00*78                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141451.00,A,3015.17762,N,11955.99110,E,0.55,5.610,021217,0.0,0,A*64                 ",
                "$GNGGA,141451.00,3015.17762,N,11957.99110,E,1,03,16.4,81.40,M,6.700,M,0.00,0000*6F         ",
                "$GNZDA,141451.00,02,12,2017,00,00*79                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141452.00,A,3015.17879,N,11955.99139,E,0.88,5.610,021217,0.0,0,A*69                 ",
                "$GNGGA,141452.00,3015.17879,N,11958.99139,E,1,03,16.4,81.50,M,6.700,M,0.00,0000*63         ",
                "$GNZDA,141452.00,02,12,2017,00,00*7A                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141453.00,A,3015.17935,N,11955.99150,E,0.91,5.610,021217,0.0,0,A*66                 ",
                "$GNGGA,141453.00,3015.17935,N,11959.99150,E,1,03,16.4,81.50,M,6.700,M,0.00,0000*64         ",
                "$GNZDA,141453.00,02,12,2017,00,00*7B                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141454.00,A,3015.18005,N,11955.99164,E,0.94,5.610,021217,0.0,0,A*66                 ",
                "$GNGGA,141454.00,3015.18005,N,11960.99164,E,1,03,16.4,81.40,M,6.700,M,0.00,0000*60         ",
                "$GNZDA,141454.00,02,12,2017,00,00*7C                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141455.00,A,3015.18048,N,11955.99174,E,0.93,5.610,021217,0.0,0,A*68                 ",
                "$GNGGA,141455.00,3015.18048,N,11961.99174,E,1,03,16.4,81.40,M,6.700,M,0.00,0000*69         ",
                "$GNZDA,141455.00,02,12,2017,00,00*7D                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141456.00,A,3015.18014,N,11955.99167,E,0.65,5.610,021217,0.0,0,A*69                 ",
                "$GNGGA,141456.00,3015.18014,N,11962.99167,E,1,03,16.4,81.40,M,6.700,M,0.00,0000*61         ",
                "$GNZDA,141456.00,02,12,2017,00,00*7E                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141457.00,A,3015.18064,N,11955.99174,E,0.69,5.610,021217,0.0,0,A*61                 ",
                "$GNGGA,141457.00,3015.18064,N,11963.99174,E,1,03,16.4,81.30,M,6.700,M,0.00,0000*62         ",
                "$GNZDA,141457.00,02,12,2017,00,00*7F                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141458.00,A,3015.18182,N,11955.99204,E,1.04,5.610,021217,0.0,0,A*69                 ",
                "$GNGGA,141458.00,3015.18182,N,11964.99204,E,1,03,16.4,81.30,M,6.700,M,0.00,0000*60         ",
                "$GNZDA,141458.00,02,12,2017,00,00*70                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141459.00,A,3015.18226,N,11955.99203,E,1.09,5.610,021217,0.0,0,A*6F                 ",
                "$GNGGA,141459.00,3015.18226,N,11965.99203,E,1,03,16.4,81.40,M,6.700,M,0.00,0000*6C         ",
                "$GNZDA,141459.00,02,12,2017,00,00*71                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141500.00,A,3015.18296,N,11955.99209,E,1.22,5.610,021217,0.0,0,A*6A                 ",
                "$GNGGA,141500.00,3015.18296,N,11966.99209,E,1,03,16.4,81.40,M,6.700,M,0.00,0000*60         ",
                "$GNZDA,141500.00,02,12,2017,00,00*7C                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141501.00,A,3015.18334,N,11955.99209,E,1.26,5.610,021217,0.0,0,A*66                 ",
                "$GNGGA,141501.00,3015.18334,N,11967.99209,E,1,03,16.4,81.40,M,6.700,M,0.00,0000*68         ",
                "$GNZDA,141501.00,02,12,2017,00,00*7D                                                       ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52",
                "$GNRMC,141502.00,A,3015.18369,N,11955.99220,E,1.27,5.610,021217,0.0,0,A*67                 ",
                "$GNGGA,141502.00,3015.18369,N,11968.99220,E,1,03,16.4,81.30,M,6.700,M,0.00,0000*6F         ",
                "$GNZDA,141502.00,02,12,2017,00,00*7E  ",
                "$GPATT,-0.00,p,0.005,r,0.000,y,20170206,s,002300345112333539343233,ID,1,INS,411,01,5,2,G*52  ",
                "$GNRMC,141503.00,A,3015.18385,N,11955.99221,E,1.25,5.610,021217,0.0,0,A*67  ",
                "$GNGGA,141503.00,3015.18385,N,11969.99221,E,1,03,16.4,81.40,M,6.700,M,0.00,0000*6A  ",
                "$GNZDA,141503.00,02,12,2017,00,00*7F  "
                )

        for item in msgs:
            time.sleep(1)
            loc = self.parse(item)
            if loc:
                if self.callback:
                    self.callback([loc.to_json()])
                print(loc)

    def read_serial(self):
        with serial.Serial(port=READ_COM, baudrate=115200) as ser:
            print("/---- COM5 start  reading")
            while self.is_running:
                if ser.inWaiting() == 0:
                    continue

                byte_line = ser.readline()
                if len(byte_line) > 0:
                    try:
                        utf_str = str(byte_line, "utf-8")
                        # print(utf_str)
                        loc = self.parse(utf_str)

                        if loc:
                            print(loc)
                            if loc.lat != 0 and loc.lng != 0 and self.callback:
                                self.callback([loc.to_json()])
                    except BaseException as ex:
                        print(ex)
                        continue

        print("/******* COM5 read exit")

    def parse(self, txt):
        bd_id = self.get_id(txt)
        if bd_id:
            self.current_id = bd_id
            if self.current_location:
                self.current_location.id = bd_id

        bd_loc = self.get_location(txt)
        if bd_loc:
            self.current_location = bd_loc
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
