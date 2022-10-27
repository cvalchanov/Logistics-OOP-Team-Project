from genericpath import exists
from src.core.data_files_manager import DataFilesManager
import unittest
from os import path, remove
from src.core.constants.path_constants import PathConstants

TEST_FILE = '../../../data-files/test_file.txt'

def fp_and_dfm():
    file_path = path.join(PathConstants.DIR_PATH, TEST_FILE)
    dfm = DataFilesManager()

    return file_path, dfm


class DataFilesManagerShould(unittest.TestCase):
    def test_read_line_for_value_returnsCorrectLineIfExists(self):
        file_path, dfm = fp_and_dfm()
        line = dfm.read_line_for_value('1', 0, file_path)

        expected = '1 This is a test file'

        self.assertEqual(expected, line)

    def test_read_line_for_value_raisesErrorIfNoLineFound(self):
        file_path, dfm = fp_and_dfm()

        with self.assertRaises(ValueError):
            line = dfm.read_line_for_value('0000000000000000000', 0, file_path)

    def test_write_line_writesCorrectly(self):
        file_path, dfm = fp_and_dfm()
        line = '6 Test Test Test'

        dfm.write_line(line, file_path)

        self.assertEqual(line, dfm.read_line_for_value('6', 0, file_path))
        dfm.remove_line(line, file_path)

    def test_update_line_updatesCorrectly(self):
        file_path, dfm = fp_and_dfm()
        line = '3 Different Test Line'
        str_to_check = '3'
        pos = 0

        dfm.update_line(line, str_to_check, pos, file_path)

        self.assertEqual(line, dfm.read_line_for_value('3', 0, file_path))
        dfm.update_line('3 Test Line', '3', 0, file_path)

    def test_remove_line_raisesErrorIfNoLineFound(self):
        file_path, dfm = fp_and_dfm()
        line = '6 Missing Test Line'

        with self.assertRaises(ValueError):
            dfm.remove_line(line, file_path)

    def test_remove_line_removesLineCorrectly(self):
        file_path, dfm = fp_and_dfm()
        lines = dfm.read_file(file_path)

        dfm.write_line('6 Test Test Test', file_path)
        dfm.remove_line('6 Test Test Test', file_path)

        self.assertEqual(lines, dfm.read_file(file_path))

    def test_read_file_returnsCorrectly(self):
        file_path, dfm = fp_and_dfm()
        expected = ['1 This is a test file', '2 Used only for the unit tests',
        '3 Test Line', '4 One more test line', '5 More test lines']

        file_content = dfm.read_file(file_path)

        self.assertEqual(expected, file_content)

    def test_create_file_createsNewFileCorrectly(self):
        dfm = DataFilesManager()
        file_path = path.join(PathConstants.DIR_PATH, '../../../data-files/temp_file.txt')

        dfm.create_file(file_path)

        self.assertTrue(exists(file_path))
        remove(file_path)

            
