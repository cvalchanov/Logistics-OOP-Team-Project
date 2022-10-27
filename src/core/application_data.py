from datetime import datetime
from os import path, remove
from src.core.constants.common_constants import CommonConstants
from src.models.location import Location
from src.models.delivery_route import DeliveryRoute
from src.core.factories.temporary_data_factory import TemporaryDataFactory
from src.models.customer import Customer
from src.models.delivery_package import DeliveryPackage
from src.core.data_files_manager import DataFilesManager
from src.models.truck import Truck
from src.core.constants.path_constants import PathConstants
from src.models.constants.truck_availability import TruckAvailability
from src.models.user import User



class ApplicationData(TemporaryDataFactory):
    PATHS_BY_TYPE = {
        DeliveryPackage : PathConstants.FILE_PATH_PACKAGE,
        DeliveryRoute : PathConstants.FILE_PATH_ROUTE,
        Truck : PathConstants.FILE_PATH_TRUCKS,
        Customer : PathConstants.FILE_PATH_CUSTOMERS,
        User : PathConstants.FILE_PATH_USERS
    }

    def __init__(self) -> None:
        self._data_files_manager = DataFilesManager()
        self._unassigned_packages: list[DeliveryPackage] = []
        self._logged_user: User = None
    
    @property
    def unassigned_packages(self):
        return tuple(self._unassigned_packages)

    @property
    def logged_user(self):
        return self._logged_user
    
    def _get_path_by_type(self, obj_type):
        if obj_type in self.PATHS_BY_TYPE:
            return path.join(PathConstants.DIR_PATH, self.PATHS_BY_TYPE[obj_type])
    
    def find_distances_file(self):
            file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_DISTANCES)
            lines = self._data_files_manager.read_file(file_path)
            return lines
 
    def find_data_by_value(self, obj_type, find_by_data):
        file_path = self._get_path_by_type(obj_type)
        try:
            line = self._data_files_manager.read_line_for_value(find_by_data, 0, file_path)
        except ValueError:
            raise ValueError(f'No object containing {find_by_data}')
        obj_info = line.split()
        obj = obj_type(*obj_info)
        return obj

    def create_object_data(self, obj_type, *data_details):
        file_path = self._get_path_by_type(obj_type)
        obj = obj_type(*data_details)
        self._data_files_manager.write_line(str(obj), file_path)
        return obj

    def remove_object_data(self, obj_type, find_by_data):
        file_path = self._get_path_by_type(obj_type)
        obj = self.find_data_by_value(obj_type, find_by_data)
        file_message = self._data_files_manager.remove_line(str(obj), file_path)
        return f'{type(obj).__name__} {file_message}'

    def view_all_objects_data(self, obj_type):
        file_path = self._get_path_by_type(obj_type)
        file_content = self._data_files_manager.read_file(file_path)
        all_objects = []

        for line in file_content:
            obj_info_line = line.split()
            obj = obj_type(*obj_info_line)
            all_objects.append(obj.info())
        
        return f'\n'.join(all_objects)

    def find_delivery_route(self, route_id):
        file_path_route = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_ROUTE)
        try:
            route_info = self._data_files_manager.read_line_for_value(route_id, 0, file_path_route)
        except ValueError:
            raise ValueError('Invalid route')
        route_details = route_info.split()
        locations = self.parse_locations(route_details)
            
        route = DeliveryRoute(route_details[0], route_details[1], route_details[2], locations, route_details[- 2], route_details[- 1])
        return route

    def parse_locations(self, route_details) -> list[Location]: 
        locations = []
        for i in range(5, len(route_details) - 2, 4):
            locations.append(Location(route_details[i - 2], route_details[i - 1], route_details[i], route_details[i + 1]))
        return locations

    def find_truck_load(self, id) -> Truck:
        truck = self.find_data_by_value(Truck, id)
        truck_path = path.join(PathConstants.FOLDER_TRUCKS_PATH, f'{id}.txt')
        file_content = self._data_files_manager.read_file(truck_path)

        for line in file_content:
            pack_info = line.split()
            pack = DeliveryPackage(int(pack_info[0]), int(pack_info[1]), int(pack_info[2]), pack_info[3], pack_info[4])
            pack.add_arrival_date_time(pack_info[5], pack_info[6])
            truck.add_package(pack)
        return truck

    def find_routes_by_condition(self, func, condition: str = None):
        routes_to_condition: list[DeliveryRoute] = []
        file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_ROUTE)
        file_content = self._data_files_manager.read_file(file_path)
        
        for line in file_content:
            route_details = line.split()
            locs = self.parse_locations(route_details)
            route = DeliveryRoute(route_details[0], route_details[1], CommonConstants.NOT_AVAILABLE, locs, route_details[- 2], route_details[- 1])
            if condition:
                func(condition, routes_to_condition, route_details, route)
            else:
                func(routes_to_condition, route_details, route)
        return routes_to_condition

    def condition_destination(self, city_abbreviation, routes_to_city, route_details, route):
        if city_abbreviation == route.find_by_abbreviation(city_abbreviation).abbreviation and route_details[2] != CommonConstants.NOT_AVAILABLE:
            truck = self.find_truck_load(route_details[2])
            route.add_truck(truck)
            routes_to_city.append(route)

    def condition_in_progress(self, routes_in_progress, route_details, route):
        if route.is_in_progress() and route_details[2] != CommonConstants.NOT_AVAILABLE:
            truck = self.find_truck_load(route_details[2])
            route.add_truck(truck)
            routes_in_progress.append(route)

    def view_available_trucks(self) -> list[str]:
        file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_TRUCKS)
        file_content = self._data_files_manager.read_file(file_path)
        available_trucks = []
        
        for line in file_content:
            truck_info = line.split()
            if truck_info[-1] == TruckAvailability.YES.upper():
                truck = Truck(truck_info[0], truck_info[1], int(truck_info[2]), int(truck_info[3]), truck_info[4])
                available_trucks.append(truck.info())
        
        return f'\n'.join(available_trucks)

    def add_truck_to_route(self, truck_id, route_id):
        route_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_ROUTE)
        route = self.find_delivery_route(route_id)
        truck = self.find_data_by_value(Truck, truck_id)
        route.add_truck(truck)
        updated_line = str(route)
        self._data_files_manager.update_line(updated_line, route_id, 0, route_path)
        return route
    
    def add_delivery_package(self, package: DeliveryPackage, truck_id, route_id):
        file_path = path.join(PathConstants.FOLDER_TRUCKS_PATH, f'{truck_id}.txt')
        route = self.find_delivery_route(route_id)
        truck = self.find_data_by_value(Truck, truck_id)
        package.add_arrival_date_time(route.arrival_date, route.arrival_time)
        truck.add_package(package)
        self._data_files_manager.write_line(str(package), file_path)
        self.remove_from_un_packages(package)
        return truck

    def create_truck(self, id, brand, capacity, range, availability) -> Truck:
        file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_TRUCKS)
        truck = Truck(id, brand, capacity, range, availability)
        truck_path = path.join(PathConstants.FOLDER_TRUCKS_PATH, f'{truck.id}.txt')
        self._data_files_manager.write_line(str(truck), file_path)
        self._data_files_manager.create_file(truck_path)
        return truck

    def remove_truck(self, id):
        file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_TRUCKS)
        truck_file_path = path.join(PathConstants.FOLDER_TRUCKS_PATH, f'{id}.txt')
        truck = self.find_data_by_value(Truck, id)

        try:
            self._data_files_manager.remove_line(str(truck), file_path)
            remove(truck_file_path)
        except FileNotFoundError:
            return f'Truck with {id} removed from list'
        return 'Truck removed successfully'

    def user_login(self, params):
        user = self.find_data_by_value(User, params[0])

        if user.password != params[1]:
            return 'Wrong password'
        
        self._logged_user = user
        return f'User {user.username} logged in successfully'

    def user_logout(self):
        self._logged_user = None

        return f'Successfully logged out'

    def update_log(self, msg):
        time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_LOG)
        line = time + msg
        self._data_files_manager.write_line(line, file_path)
        
    def view_log(self, date):
        file_path = path.join(PathConstants.DIR_PATH, PathConstants.FILE_PATH_LOG)
        log_content = self._data_files_manager.read_file(file_path)
        date_log_entries = []
        for line in log_content:
            line_info = line.split()
            if line_info[0] == date:
                date_log_entries.append(line)

        return '\n'.join(date_log_entries)       

