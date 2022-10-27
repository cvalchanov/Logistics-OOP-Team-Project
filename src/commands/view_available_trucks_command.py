from src.core.application_data import ApplicationData
from os import path

class ViewAvailableTrucksCommand:
    def __init__(self, data: ApplicationData):
        self._app_data = data


    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')
            
        msg = self._app_data.view_available_trucks()
        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed available trucks')
        return msg



    