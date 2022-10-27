from src.core.application_data import ApplicationData

class ViewTruckLoadCommand:
    def __init__(self, params, data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        try:
            truck_id = self._params[0]
            truck = self._app_data.find_truck_load(truck_id)
        except ValueError:
            return f'No truck with ID {truck_id} found!'

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed the load of truck with ID: {truck_id}')
        return truck.load_info()
