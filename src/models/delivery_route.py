import datetime
from src.core.constants.common_constants import CommonConstants
from src.models.location import Location
from src.models.truck import Truck
from src.models.delivery_package import DeliveryPackage


class DeliveryRoute:
    def __init__(self, id, total_distance, truck, locations: list[Location], arrival_date, arrival_time) -> None:
        self._id = id
        if len(locations) < 2:
            raise ValueError('Locations should be at least two')
        self._locations = locations
        self._total_distance = total_distance
        self._truck = truck
        self._arrival_date = arrival_date
        self._arrival_time = arrival_time

    @property
    def id(self):
        return self._id
    
    @property
    def arrival_date(self):
        return self._arrival_date

    @property
    def arrival_time(self):
        return self._arrival_time

    def find_by_abbreviation(self, abbreviation):
        for loc in range(1, len(self._locations)):
            if self._locations[loc].abbreviation == abbreviation:
                return self._locations[loc]

    
    def is_in_progress(self):
        if self._locations[0].is_in_progress():
            return True
        return False

    def get_truck_id(self):
        return self._truck.id

    def find_package_in_truck(self, id):
        for pack in self._truck.load:
            if pack.id == id:
                return pack

    def find_current_stop(self):
        in_progress = []
        for loc in self._locations:
            if loc.is_in_progress():
                in_progress.append(loc)
        if not in_progress:
            return None
        return in_progress[-1]

    def add_delivery_package(self, package: DeliveryPackage):
        self._truck.add_package(package)

    def add_truck(self, truck: Truck):
        self._truck = truck
    
    def __str__(self) -> str:
        locs = ' '.join(map(str, self._locations))
        output = f'{self._id} {self._total_distance}'
        if isinstance(self._truck, Truck):
            output = f'{output} {self._truck.id}'
        else:
            output = f'{output} {CommonConstants.NOT_AVAILABLE}'
        output = f'{output} {locs} {self._arrival_date} {self._arrival_time}'

        return output

    def locations_info(self):
        locs = ' -> '.join([loc.info() for loc in self._locations])
        return locs

    def info(self):
        locs = self.locations_info()
        output = f'Delivery Rout ID: {self._id}'
        if isinstance(self._truck, Truck):
            output = f'{output} Truck ID: {self._truck.id}'
        else:
            output = f'{output} Truck ID: N/A'
        output = f'{output} Total Distance: {self._total_distance} Arrival Time: {self._arrival_date} {self._arrival_time} Locations: {locs}'

        return output
    
    def in_progress_info(self):
        if not self.is_in_progress():
            raise ValueError(f'Route #{self._id} not in progress')

        current_stop = self.find_current_stop()
        if current_stop == None:
            raise ValueError(f'Route #{self._id} not in progress')
        weight = self._truck.get_total_weight()
        locs = self.locations_info()
        output = f'Locations: {locs} Delivery Weight: {weight} kg Current Stop: {current_stop}'
        return output
