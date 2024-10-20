import unittest
import configparser
from app import ShellEmulator

class TestShellEmulator(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.shell = ShellEmulator(config["settings"])

    def test_ls_with_no_arguments(self):
        expected_output = "file1.txt\nfile2.txt\nfile3.txt\npictures\n"
        result = self.shell.ls([])
        self.assertEqual(result, expected_output)

    def test_ls_with_valid_directory(self):
        expected_output = "pic (1).jpg\npic (2).jpg\npic (3).jpg\nsmaller_pictures\n"
        result = self.shell.ls(["pictures"])
        self.assertEqual(result, expected_output)

    def test_ls_with_invalid_directory(self):
        expected_output = "Директория не содержит файлы или не существует\n"
        result = self.shell.ls(["dir"])
        self.assertEqual(result, expected_output)

    def test_pwd_1(self):
        result = self.shell.pwd()
        self.assertEqual(result, '/')

    def test_cd_to_valid_directory_1(self):
        result = self.shell.cd(["pictures"])
        self.assertEqual(result, "")
        self.assertEqual(self.shell._cur_path, '/pictures')

    def test_pwd_2(self):
        self.test_cd_to_valid_directory_1()
        result = self.shell.pwd()
        self.assertEqual(result, '/pictures') 

    def test_cd_to_valid_directory_2(self):
        result = self.shell.cd(["/pictures/smaller_pictures"])
        self.assertEqual(result, "")
        self.assertEqual(self.shell._cur_path, '/pictures/smaller_pictures')

    def test_pwd_3(self):
        self.test_cd_to_valid_directory_2()
        result = self.shell.pwd()
        self.assertEqual(result, '/pictures/smaller_pictures') 

    def test_cd_to_invalid_directory(self):
        result = self.shell.cd(["dir"])
        self.assertEqual(result, "Некорректный путь\n")

    def test_cal_without_arguments(self):
        result = self.shell.cal([])
        self.assertIn('2024', result)
        self.assertIn('October', result)

    def test_cal_with_year_argument(self):
        result = self.shell.cal(['2000'])
        self.assertIn('2000', result)

    def test_cal_with_month_and_year_arguments(self):
        result = self.shell.cal(['2', '2022'])
        self.assertIn('February', result)
        self.assertIn('2022', result)

if __name__ == "__main__":
    unittest.main()