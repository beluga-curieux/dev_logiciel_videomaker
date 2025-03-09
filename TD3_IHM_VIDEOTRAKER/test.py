import filePath
import unittest
from point import Point, Timescale

class TestPoint(unittest.TestCase):
    def test_creation_points(self):
        x,y = 12, -14
        tms = Timescale(1)
        p = Point(x, y, tms)
        self.assertEqual(p.get_x(), 12)
        self.assertEqual(p.get_y(), -14)
        self.assertEqual(p.get_timescale(), tms)



class TestFilePathAndPoint(unittest.TestCase):
    def test_creation_FilePath(self):
        file_path = filePath.FilePath('doc/test.csv')
        self.assertEqual(str(file_path), 'doc/test.csv')

    def test_set_file_path(self):
        chemin = filePath.FilePath("test.csv")
        chemin.set_file_path("test2.csv")
        self.assertEqual(str(chemin), "test2.csv")

    def test_write_in_file(self):
        chemin_nonexistant = filePath.FilePath("nonexisant/testfaux.csv")
        self.assertEqual(chemin_nonexistant.write_in_file("r"), False)

        chemin = filePath.FilePath("test.csv")
        chemin.write_in_file("t")
        with open(str(chemin), "r") as file:
            self.assertEqual(file.read(), "t", "Le texte n'a pas bien été écrit")

    def test_convert_to_csv(self):
        file_path = filePath.FilePath('')
        points = [
            Point(i * 11, i * -11, Timescale(i)) for i in range(0, 5)
        ]

        self.assertEqual(file_path.convert_to_csv(points),
                     "0;0;0\n11;-11;1\n22;-22;2\n33;-33;3\n44;-44;4\n",
                         'la function convert_to_csv ne fonctione pas')

        self.assertEqual(file_path.convert_to_csv([]),
                         "",
                         'la function convert_to_csv ne fonctione pas')

    def test_file_allready_exist(self):
        with open("test.csv", "r") as file:
            pass
        chemin_existant = filePath.FilePath("test.csv")
        chemin_nonexistant = filePath.FilePath("testfaux.csv")
        self.assertEqual(chemin_existant.file_allready_exist(), True)
        self.assertEqual(chemin_nonexistant.file_allready_exist(), False)




if __name__ == '__main__':
    unittest.main()