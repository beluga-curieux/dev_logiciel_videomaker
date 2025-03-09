import datetime
import time


class Point:
    def __init__(self, x, y, timescale):
        self.__x=x
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

class FilePath:
    def __init__(self, path):
        self.__path = path

    def convert_to_csv(self, points):
        textcsv=''
        for i in range(len(points)):
            textcsv += str(points[i].get_x()) + ";" + str(points[i].get_y()) + ";" + str(points[i].get_timescale().get_time()) + "\n"
        return textcsv

    def set_path(self, path):
        self.__path = path

    def export_to_csv(self, file_name:str, data_csv:str):
        if not (self.chek_repertory_path()
                and  (not self.file_allready_exist(file_name))
                and self.make_file(file_name)
                and self.write_in_file(file_name, data_csv) ):

            return False

    def chek_repertory_path(self):
        pass

    def file_allready_exist(self, file_name):
        pass

    def make_file(self, file_name):
        pass

    def write_in_file(self, file_name, text):
        pass


if __name__ == '__main__':
    fichier=FilePath("Coucoupapjet'appelle bisous")
    P1=Point(4,4, Timescale(1))
    P2 = Point(8, 44, Timescale(7))
    P3 = Point(465, 94, Timescale(8))
    P4 = Point(7, 99, Timescale(188))
    listeP=[P1,P2,P3,P4]
    cvs=fichier.convert_to_csv(listeP)
    print(cvs)
