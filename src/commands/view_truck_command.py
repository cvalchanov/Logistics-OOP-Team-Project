from src.models.truck import Truck
from src.core.application_data import ApplicationData

class ViewTruckCommand:
    def __init__(self, params, data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        truck_id = self._params[0]
        try:
            truck = self._app_data.find_data_by_value(Truck,truck_id)
        except ValueError:
            return f'No truck with ID {truck_id} found!'

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed truck with ID: {truck_id}')            
        return truck.info()
