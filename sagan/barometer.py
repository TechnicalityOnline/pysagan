from .i2c import I2cDevice

BME280_REGISTER_T1 = 0x88  # Trimming parameter registers
BME280_REGISTER_T2 = 0x8A
BME280_REGISTER_T3 = 0x8C

BME280_REGISTER_P1 = 0x8E
BME280_REGISTER_P2 = 0x90
BME280_REGISTER_P3 = 0x92
BME280_REGISTER_P4 = 0x94
BME280_REGISTER_P5 = 0x96
BME280_REGISTER_P6 = 0x98
BME280_REGISTER_P7 = 0x9A
BME280_REGISTER_P8 = 0x9C
BME280_REGISTER_P9 = 0x9E

BME280_REGISTER_H1 = 0xA1
BME280_REGISTER_H2 = 0xE1
BME280_REGISTER_H3 = 0xE3
BME280_REGISTER_H4 = 0xE4
BME280_REGISTER_H5 = 0xE5
BME280_REGISTER_H6 = 0xE6
BME280_REGISTER_H7 = 0xE7

BME280_REGISTER_CHIPID = 0xD0
BME280_REGISTER_VERSION = 0xD1
BME280_REGISTER_SOFTRESET = 0xE0

BME280_REGISTER_CONTROL_HUM = 0xF2
BME280_REGISTER_CONTROL = 0xF4
BME280_REGISTER_CONFIG = 0xF5
BME280_REGISTER_PRESSURE_DATA = 0xF7
BME280_REGISTER_TEMP_DATA = 0xFA
BME280_REGISTER_HUMIDITY_DATA = 0xFD


class Barometer(I2cDevice):
    data_frame = '<HBHBH'

    """
    Interface for BME280 pressure and humidity
    """
    def measure(self):
        frame = self.read_and_unpack(0xF7, self.data_frame)
        return frame

    def test(self):
        id, = self.read_and_unpack(BME280_REGISTER_CHIPID, 'B')
        return id == 0x60

    def configure(self):
        mode = 0b11 # 'Normal' mode
        pressure_oversample = 1
        temperature_oversample = 1
        humidity_oversample = 1
        ctrl_meas = (temperature_oversample << 5) | (pressure_oversample << 2) | mode
        ctrl_hum = humidity_oversample & 0b00000111
        self.pack_and_write(0xF4, 'B', ctrl_meas)
        self.pack_and_write(0xF2, 'B', ctrl_hum)