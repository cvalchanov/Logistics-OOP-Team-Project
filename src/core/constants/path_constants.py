from os import path


class PathConstants:
   DIR_PATH = path.dirname(__file__)
   FILE_PATH_PACKAGE = '../../../data-files/delivery_package_data.txt'
   FILE_PATH_ROUTE = '../../../data-files/delivery_routes_data.txt'
   FILE_PATH_DISTANCES = '../../../data-files/distances.txt'
   FILE_PATH_TRUCKS = '../../../data-files/trucks_data.txt'
   FILE_PATH_IDS = '../../../data-files/ids_data.txt'
   FILE_PATH_CUSTOMERS = '../../../data-files/customers_data.txt'
   FILE_PATH_USERS = '../../../data-files/users_data.txt'
   FILE_PATH_LOG = '../../../data-files/system_log.txt'
   FOLDER_TRUCKS_PATH = path.join(DIR_PATH, '../../../data-files/trucks/')

