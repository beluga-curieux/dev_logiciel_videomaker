
class Point:
    def __init__(self, x, y, timescale):
        self.__x = x
        self.__y = y
        self.__timescale = timescale

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_timescale(self):
        return self.__timescale

class Timescale:
    def __init__(self,time_start):
        self.__time = time_start

    def get_time(self):
        return self.__time