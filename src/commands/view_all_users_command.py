from src.models.user import User
from src.core.application_data import ApplicationData
from src.models.constants.user_roles import UserRoles

class ViewAllUsersCommand:
    def __init__(self, data: ApplicationData) -> None:
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role == UserRoles.EMPLOYEE:
            raise ValueError('Employess can\'t view other employees')

        msg = self._app_data.view_all_objects_data(User)
        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed all users')
        return msg