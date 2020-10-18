"""
Simple solution
"""
from math import pow, sqrt

link_station = [[0, 0, 10], [20, 20, 5], [10, 0, 12]]
device_points = [[0, 0], [100, 100], [15, 10], [18, 18]]


def get_dev_link_dist(link, device):
    """
    :param link: list of link station coordinate [x, y]
    :param device: list representing a device coordinate [x, y]
    :return: float, 2-d distance
    """
    return sqrt(pow(device[0] - link[0], 2) + pow(device[1] - link[1], 2))


def get_power(reach, distance):
    """
    :param reach: float or int, link station coverage
    :param distance: float, distance between a device and a link station
    :return: float, power of the coverage
    """
    return 0.0 if distance > reach else pow(reach - distance, 2)


def printer(device, best_link_station, power):
    """
    :param device: list representing a device coordinate [x, y]
    :param best_link_station: list of coordinates x,y of the best station
    :param power: float, best power
    :return: printer
    """
    if power != 0:
        print("Best link station for point {},{} is {},{} with power {}".format(device[0], device[1],
                                                                                best_link_station[0],
                                                                                best_link_station[1], power))
    else:
        print("No link station within reach for point {},{}".format(device[0], device[1]))


def find_link_station(links, device):
    """
    :param links: list of lists, link stations coordinates and reach [x, y, z]
    :param device: list representing a device coordinate [x, y]
    :return: String, Best match link station for a device
    """
    max_power_inx = 0
    max_power = get_power(links[0][2], get_dev_link_dist(links[0][:2], device))
    for i in range(1, len(links)):
        current_power = get_power(links[i][2], get_dev_link_dist(links[i][:2], device))
        if current_power > max_power:
            max_power_inx = i
            max_power = current_power
    return printer(device, links[max_power_inx][:2], max_power)


if __name__ == '__main__':
    for j in range(len(device_points)):
        find_link_station(link_station, device_points[j])
