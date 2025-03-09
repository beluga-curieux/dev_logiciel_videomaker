import datetime
import time
import os

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

class FilePath:
    def __init__(self, file_path):
        self.__file_path = file_path

    def __str__(self):
        return self.__file_path

    def convert_to_csv(self, points):
        text_csv = ''
        for i in range(len(points)):
            text_csv += (str(points[i].get_x())
                         + ";" + str(points[i].get_y())
                         + ";" + str(points[i].get_timescale().get_time())
                         + "\n")
        return text_csv

    def set_file_path(self, file_path):
        self.__file_path = file_path

    def export_to_csv(self, data_csv:str):
        if not (self.check_repertory_path()
                and  (not self.file_allready_exist())
                and self.write_in_file(data_csv) ):

            return False

    def check_repertory_path(self) -> bool:
        directory = os.path.dirname(self.__file_path)

        if not directory:
            return True

        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except Exception as err:
                print(f"check_repertory_path error :", err)
                return False

        return True

    def file_allready_exist(self):
        return os.path.exists(self.__file_path)

    def write_in_file(self, text):
        if not self.__file_path.endswith(".csv"):
            self.__file_path += ".csv"
        try :
            with open(self.__file_path, "w") as file:
                file.write(text)

            return True

        except Exception as err:
            print("write_in_file error :", err)

            return False

if __name__ == '__main__':

    fichier = FilePath("maman")

    P1 = Point(4,4, Timescale(1))
    P2 = Point(8, 44, Timescale(7))
    P3 = Point(465, 94, Timescale(8))
    P4 = Point(7, 99, Timescale(188))

    listeP = [P1,P2,P3,P4]
    cvs = fichier.convert_to_csv(listeP)
    fichier.export_to_csv(cvs)
    print(cvs)
