import serial

from map.templates.BDReceiver import BDReceiver

is_reading = True


def read_serial():
    ser = serial.Serial(  # 下面这些参数根据情况修改
        port='COM5',
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=5,
    )
    bd = BDReceiver()
    while ser.inWaiting() > 0:
        # read_bytes = ser.read(256)
        byte_line = ser.readline()
        if len(byte_line) > 0:
            str_len = str(byte_line, "utf-8")
            loc = bd.parse(str_len)
            print(byte_line)


if __name__ == "__main__":
    read_serial()
    a = input("press any key to stop radar receiver:")
