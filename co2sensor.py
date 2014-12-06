import time

import serial


class Co2Sensor:
    """
    Classe definissant le capteur de CO2 ainsi que les methodes de lecture de la concentration de CO2
    """

    read_sequence = chr(0xFE) + chr(0x04) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x01) + chr(0x25) + chr(0xC5)

    sensor_speed = 19200
    sensor_bytesize = serial.EIGHTBITS
    sensor_port = "\\dev\\ttyUSB0"
    sensor_parity = serial.PARITY_NONE
    sensor_stopbits = serial.STOPBITS_ONE

    sensor_con = serial.Serial()

    def __init__(self):
        return

    def connect(self):
        """
        :arg self
        :return status

        Demarre le connexion serie avec la capteur
        """
        status = False

        if self.sensor_con.isOpen():
            self.sensor_con.close()

        self.sensor_con.port = self.sensor_port
        self.sensor_con.baudrate = self.sensor_speed
        self.sensor_con.bytesize = self.sensor_bytesize
        self.sensor_con.parity = self.sensor_parity
        self.sensor_con.stopbits = self.sensor_stopbits

        self.sensor_con.open()

        if self.sensor_con.isOpen():
            status = True

        return status

    def configure(self, port=sensor_port, speed=sensor_speed, bytesize=sensor_bytesize,
                  parity=sensor_parity, stopbits=sensor_stopbits):
        """
        Reconfiguration de la liaison serie
        :param port:
        :param speed:
        :param bytesize:
        :param parity:
        :param stopbits:
        :return:
        """

        self.sensor_port = port
        self.sensor_speed = speed
        self.sensor_bytesize = bytesize
        self.sensor_parity = parity
        self.sensor_stopbits = stopbits

    def read(self):
        """
        Lecture de la concentration de CO2
        :return:
        """

        self.sensor_con.write(self.read_sequence)
        time.sleep(5)
        return self.sensor_con.read(self.sensor_con.inWaiting())