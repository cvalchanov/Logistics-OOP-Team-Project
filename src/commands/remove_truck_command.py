from src.models.constants.user_roles import UserRoles
from src.core.application_data import ApplicationData

class RemoveTruckCommand:
    def __init__(self, params, data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role != UserRoles.MANAGER:
            raise ValueError('Only managers can remove trucks')

        if len(self._params) != 1:
            raise ValueError('Indaliv Input')

        try:
            msg = self._app_data.remove_truck(self._params[0])
        except ValueError:
            return f'No truck with ID {self._params[0]} found!'

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - removed truck with ID: {self._params[0]}')
        return msg        