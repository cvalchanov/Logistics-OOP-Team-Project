from src.core.application_data import ApplicationData
from src.models.constants.user_roles import UserRoles

class ViewLogCommand:
    def __init__(self, params: list[str], data: ApplicationData) -> None:
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role == UserRoles.EMPLOYEE:
            raise ValueError('Employess can\'t view the log')
        
        if len(self._params) != 1:
            return 'Invalid input'

        date = self._params[0]

        msg = self._app_data.view_log(date)

        if len(msg) > 0:
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed the log')
            return msg

        return 'No entries found for that date'        
