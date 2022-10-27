
from src.core.application_data import ApplicationData

class AddTruckToRouteCommand:
    def __init__(self, params, data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')
        
        if len(self._params) != 2:
            return 'Invalid input'

        truck_id = self._params[0]
        route_id = self._params[1]

        try:
            route = self._app_data.add_truck_to_route(truck_id, route_id)
            msg = f'Truck {route.get_truck_id()} added to route {route.id}'
        except:
            msg = 'No such route or truck found'
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - {msg}')
            return msg

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - {msg}')            
        return msg
