# Name: J. Lewis

import math
import numpy as np


def distance(point1, point2):
    """
    Calculates the distance between two points.
    :param point1: A coordinate pair (x, y).
    :param point2: A coordinate pair (x, y).
    :return: The distance between two pairs of coordinates.
    """
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


if __name__ == '__main__':
    home_input = input("Enter the coordinates of your home location, as a pair of numbers: x,y: ")

    x, y = home_input.split(",")
    x = float(x); y = float(y)
    home_location = (x, y, "Home")

    business_locations = np.zeros(3, dtype={'names':('x', 'y', 'name'), 'formats':('f4', 'f4', 'U10')})
    business_locations['x'] = [7.5, 1.2, 4.0]
    business_locations['y'] = [12.0, 9.7, 6.3]
    business_locations['name'] = ["Denver", "Golden", "Lakewood"]

    business_distances = [(distance(home_location, business), business[2]) for business in business_locations]
    business_distances = sorted(business_distances)

    print(f"The closest location to your home is {business_distances[0][1]}, {business_distances[0][0]:.2f} mi away.")

