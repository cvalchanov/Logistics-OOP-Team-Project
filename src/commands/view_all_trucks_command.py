from src.models.truck import Truck
from src.core.application_data import ApplicationData

class ViewAllTrucksCommand:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        msg = self._app_data.view_all_objects_data(Truck)
        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed all trucks')
        return msg
