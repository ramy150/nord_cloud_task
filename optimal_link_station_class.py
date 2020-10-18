"""
Solution based on classes
"""

from math import pow, sqrt


class Device:
    def __init__(self, x, y):
        """
        The constructor of Device
        :param x: coordinate x
        :param y: coordinate y
        """
        self.x = x
        self.y = y

    def set(self, value_x, value_y):
        """
        :param value_x: coordinate x
        :param value_y: coordinate y
        :return: modified values of x and y coordinates
        """
        print('Updating', self.x, 'and', self.y)
        self.x = value_x
        self.y = value_y

    def get(self):
        """
        :return: current x and y coordinates
        """
        print('Retrieving', self.x, 'and', self.y)
        return self.x, self.y

    def get_dev_link_dist(self, extrenal):
        """
        :param extrenal: list of link station coordinate [x, y]
        :return: float, 2-d distance
        """
        return sqrt(pow(self.x - extrenal.x, 2) + pow(self.y - extrenal.y, 2))

    def printer(self, best_link_station, power):
        """
        :param best_link_station: list of coordinates x,y of the best station
        :param power: float, best power
        :return: printer function
        """
        if power != 0:
            print("Best link station for point {},{} is {},{} with power {}".format(self.x, self.y,
                                                                                    best_link_station.x,
                                                                                    best_link_station.y, power))
        else:
            print("No link station within reach for point {},{}".format(self.x, self.y))

    def find_link_station(self, link_stations):
        """
        :param link_stations: list of link_station instances (link stations coordinates and reach [x, y, z])
        :return: String, Best match link station for a device
        """
        max_power_inx = 0
        max_power = 0
        for link_station in link_stations:
            current_power = link_station.get_power(self)
            if current_power > max_power:
                max_power_inx = link_station
                max_power = current_power
        return self.printer(max_power_inx, max_power)


class LinkStation(Device):
    def __init__(self, x, y, reach):
        """
        The constructor of Link Station
        :param x: coordinate x
        :param y: coordinate y
        :param reach: coverage
        """
        Device.__init__(self, x, y)
        self.reach = reach

    def get_link_dev_dist(self, external):
        """
        :param external: device instance coordinate (x, y)
        :return: float, 2-d distance
        """
        return sqrt(pow(self.x - external.x, 2) + pow(self.y - external.y, 2))

    def get_power(self, external):
        """
        :param external: device instance coordinate (x, y)
        :return: float, power of the coverage
        """
        distance = self.get_link_dev_dist(external)
        return 0.0 if distance > self.reach else pow(self.reach - distance, 2)


def test_func():
    link_stations_ = [
        LinkStation(0, 0, 10),
        LinkStation(20, 20, 5),
        LinkStation(10, 0, 12)
    ]
    devices = [
        Device(0, 0),
        Device(100, 100),
        Device(15, 10),
        Device(18, 18)
    ]

    for device in devices:
        device.find_link_station(link_stations_)


if __name__ == '__main__':
    test_func()
