# Great distance formula ported to python from formula given
from math import radians, acos, sin, cos
def getDistanceBetweenCoordinates(lat1, long1, lat2, long2):
        long1, lat1, long2, lat2 = map(radians, [long1, lat1, long2, lat2])
        r = 6373
        distance = (acos((sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))) * r)
        return distance

