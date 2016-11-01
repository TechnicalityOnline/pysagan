import smbus


class I2cDevice:
    """
    A light wrapper on top of smbus for convenience.
    """
    def __init__(self, bus: smbus.SMBus, address):
        self.bus = bus
        self.address = address

    def read(self, cmd, length):
        return self.bus.read_i2c_block_data(self.address, cmd, length)

    def write(self, cmd, values):
        return self.bus.write_i2c_block_data(self.address, cmd, values)
