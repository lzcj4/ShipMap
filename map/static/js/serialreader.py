import serial


is_reading=True;
def read_serial():
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
        read_line = ser.readline()
        if len(read_line) > 0:
            print(read_line)


if __name__ == "__main__":
    read_serial()
    a = input("press any key to stop radar receiver:")
