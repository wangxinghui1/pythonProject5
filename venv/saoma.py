import binascii
from binascii import hexlify
import codecs
import struct
import serial
import threading
import multiprocessing
import logging
import time
import serial.tools.list_ports
serialport=serial.Serial('COM7',115200,timeout=0.5)
def print_ports():
    port_list=list(serial.tools.list_ports.comports())
    if len(port_list)==0:
        print("找不到串口")
    else:
        for i in range(0,len(port_list)):
            print(port_list[i])
def serialserver():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    count = 0
    while True:
        try:
            data = serialport.readall()
            if data != b'':
                if data[4:8]==b'\x10\x00\x01\x01':
                  serialport.write(data1)
                  re1=data.hex()
                  logging.info(re1)
                if data[4:8]==b'\x00\x00\x00\x17':
                  serialport.write(datachuka)
                  logging.info(data.hex())
                  logging.info(data[7:14].decode('utf-8'))
                  count += 1
                  logging.info(count)
        except Exception as ex:
            print(ex)
        if count>100:
             break
if __name__=="__main__":
    # 发送数据
    datachuka=b'\xFF\xFF\x00\x0A\x10\x00\x01\x01\x1c\xFE'
    data1 = b'\xFF\xFF\x00\x0A\x00\x00\x00\x17\x21\xFE'
    print("串口列表")
    print_ports()
    p=threading.Thread(target=serialserver,args=())
    p.start()
    serialport.write(datachuka)
    p.join()