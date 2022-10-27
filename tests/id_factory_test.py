import unittest
from src.core.factories.id_factory import IDFactory
from os import path
from src.core.data_files_manager import DataFilesManager
from src.core.constants.path_constants import PathConstants

def dfm_and_path():
    dfm = DataFilesManager()
    file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_IDS)

    return dfm, file_path


class IDFactoryShould(unittest.TestCase):
    def test_get_ids_returnsCorrectValues(self):
        dfm, file_path = dfm_and_path()
        file_content = dfm.read_file(file_path)
        expected = []

        for line in file_content:
            line_con = line.split()
            id = int(line_con[1])
            expected.append(id)

        ids = IDFactory.get_ids()

        self.assertEqual(expected, ids)

    def test_update_id_updatesWithCorrectValues(self):
        dfm, file_path = dfm_and_path()
        file_content = dfm.read_file(file_path)
        real_ids = []
        fake_ids = [1000, 1000, 1000, 1000]

        for line in file_content:
            line_con = line.split()
            id = int(line_con[1])
            real_ids.append(id)

        IDFactory.update_id(fake_ids)
        updated_ids = IDFactory.get_ids()

        IDFactory.update_id(real_ids)
        self.assertEqual(fake_ids, updated_ids)

    def test_get_truck_id_returnsCorrectID(self):
        dfm, file_path = dfm_and_path()
        file_content = dfm.read_file(file_path)
        real_ids = []               

        for line in file_content:
            line_con = line.split()
            id = int(line_con[1])
            real_ids.append(id)

        expected = real_ids[0] + 1
        truck_id = IDFactory.get_truck_id()

        IDFactory.update_id(real_ids)
        self.assertEqual(expected, truck_id)

    def test_get_package_id_returnsCorrectID(self):
        dfm, file_path = dfm_and_path()
        file_content = dfm.read_file(file_path)
        real_ids = []               

        for line in file_content:
            line_con = line.split()
            id = int(line_con[1])
            real_ids.append(id)

        expected = real_ids[1] + 1
        package_id = IDFactory.get_package_id()

        IDFactory.update_id(real_ids)
        self.assertEqual(expected, package_id)

    def test_get_route_id_returnsCorrectID(self):
        dfm, file_path = dfm_and_path()
        file_content = dfm.read_file(file_path)
        real_ids = []               

        for line in file_content:
            line_con = line.split()
            id = int(line_con[1])
            real_ids.append(id)

        expected = real_ids[2] + 1
        route_id = IDFactory.get_route_id()

        IDFactory.update_id(real_ids)
        self.assertEqual(expected, route_id)

    def test_get_customer_id_returnsCorrectID(self):
        dfm, file_path = dfm_and_path()
        file_content = dfm.read_file(file_path)
        real_ids = []               

        for line in file_content:
            line_con = line.split()
            id = int(line_con[1])
            real_ids.append(id)

        expected = real_ids[3] + 1
        customer_id = IDFactory.get_customer_id()

        IDFactory.update_id(real_ids)
        self.assertEqual(expected, customer_id)