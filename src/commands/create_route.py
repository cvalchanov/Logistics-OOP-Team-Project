from datetime import datetime
from src.core.constants.common_constants import CommonConstants
from src.models.location import Location
from src.models.delivery_route import DeliveryRoute
from src.core.factories.id_factory import IDFactory
from src.core.location_factory import LocationFactory
from src.core.application_data import ApplicationData


class CreateRouteCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        self._params = params
        self._app_data = app_data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')
        
        if len(self._params) < 4:
            return 'Invalid input'

        date_1, time_1 , *cities = self._params
        id = IDFactory.get_route_id()
        date_time = self.validate_date_time_format(date_1, time_1)

        lines = self._app_data.find_distances_file()
        distances = LocationFactory.calculate_distances(cities, lines, True)
        total_dist = sum(distances) 
        locations = self._add_locations(date_time, cities, distances)

        route = self._app_data.create_object_data(DeliveryRoute, id, total_dist, CommonConstants.NOT_AVAILABLE, locations, locations[-1].date_in_location, locations[-1].time_in_location)
        self._app_data.update_log(f' - {self._app_data.logged_user.username} - created delivery route #{route.id}')    
        return f'Delivery route #{route.id} was created.'

    def _add_locations(self, date_time, cities, distances):
        locations: list[Location] = []

        for i in range(len(cities)):
            time_in_loc = LocationFactory.calculate_location_time(date_time, distances[i])
            loc = LocationFactory.create_location_by_abrreviation(cities[i], time_in_loc.date().strftime('%Y-%m-%d'), time_in_loc.time().strftime('%H:%M'))
            locations.append(loc)
            date_time = time_in_loc
            
        return locations

    def validate_date_time_format(self, arrival_date, arrival_time):
        try:
            date_time = datetime.strptime(f'{arrival_date} {arrival_time}', '%Y-%m-%d %H:%M')
            return date_time
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD H:MM")