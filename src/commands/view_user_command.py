from src.models.user import User
from src.core.application_data import ApplicationData
from src.models.constants.user_roles import UserRoles

class ViewUserCommand:
    def __init__(self, params: list[str], data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role == UserRoles.EMPLOYEE:
            raise ValueError('Employess can\'t view other employees')

        username = self._params[0].lower()
        try:
            user = self._app_data.find_data_by_value(User, username)
        except ValueError:
            return f'No user with username {username} found!'

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed user with username {username}')            
        return user.info()