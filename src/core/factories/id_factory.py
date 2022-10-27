from src.core.constants.path_constants import PathConstants
from os import path

class IDFactory:
    @classmethod
    def get_ids(cls):
        file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_IDS)
        ids = []
        with open(file_path, mode='r') as file:
            for line in file:
                info = line.split()
                id = int(info[-1])
                ids.append(id)

        return ids

    @classmethod
    def update_id(cls, ids):
        file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_IDS)
        with open(file_path, mode='w') as file:
            file.write(f'truck_id {ids[0]}\npackage_id {ids[1]}\nroute_id {ids[2]}\ncustomer_id {ids[3]}')
                                                
    @classmethod
    def get_truck_id(cls):
        ids = cls.get_ids()
        truck_id = ids[0] + 1
        ids[0] = truck_id
        cls.update_id(ids)
        return truck_id

    @classmethod
    def get_package_id(cls):
        ids = cls.get_ids()
        package_id = ids[1] + 1
        ids[1] = package_id
        cls.update_id(ids)
        return package_id

    @classmethod
    def get_route_id(cls):
        ids = cls.get_ids()
        route_id = ids[2] + 1
        ids[2] = route_id
        cls.update_id(ids)
        return route_id
            
    @classmethod
    def get_customer_id(cls):
        ids = cls.get_ids()
        customer_id = ids[3] + 1
        ids[3] = customer_id
        cls.update_id(ids)
        return customer_id