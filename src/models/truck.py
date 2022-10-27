from src.models.constants.truck_availability import TruckAvailability
from os import path
from src.core.constants.path_constants import PathConstants
from src.models.delivery_package import DeliveryPackage
from src.core.data_files_manager import DataFilesManager

class Truck:

    def __init__(self, truck_id, brand, capacity, range, availabe):
        self._truck_id = truck_id
        self._brand = brand
        self._capacity = int(capacity)
        self._range = range
        self.available = availabe
        self._load: list[DeliveryPackage] = []

    @property
    def load(self):
        return tuple(self._load)

    @property
    def id(self):
        return self._truck_id

    @property
    def brand(self):
        return self._brand

    @property
    def capacity(self):
        return self._capacity

    @property
    def range(self):
        return self._range

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value: str):
        if value.lower() == 'yes':
            self._available = TruckAvailability.YES
        elif value.lower() == 'no':
            self._available = TruckAvailability.NO
        else:
            raise ValueError(f'Truck availability can be only {TruckAvailability.YES} or {TruckAvailability.NO}')

    def add_package(self, package: DeliveryPackage): 
        if package.weight + self.get_total_weight() > self.capacity:
            raise ValueError('The package exceeds this truck capacity.')
        self._load.append(package)

    def get_total_weight(self):
        return sum([x.weight for x in self._load])            

    def __str__(self):
        return f'{self.id} {self.brand} {self.capacity} {self.range} {self.available.upper()}'
    
    def info(self):
        return f'ID:{self.id} - {self.brand}. Maximum capacity: {self.capacity}. Maximum Range: {self.range}. Availability: {self.available.upper()}'

    def load_info(self):
        output = '\n'.join([f'{x + 1}. {self._load[x].info()}' for x in range(len(self._load))])
        return output

            