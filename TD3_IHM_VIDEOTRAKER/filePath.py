import os

class FilePath:
    def __init__(self, file_path):
        self.__file_path = file_path

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