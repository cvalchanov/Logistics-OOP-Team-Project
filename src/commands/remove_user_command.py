from src.models.user import User
from src.core.application_data import ApplicationData
from src.models.constants.user_roles import UserRoles

class RemoveUserCommand:
    def __init__(self, params, data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role != UserRoles.MANAGER:
            raise ValueError('Only managers can remove users')

        if len(self._params) != 1:
            raise ValueError('Indaliv Input')

        try:
            msg = self._app_data.remove_object_data(User, self._params[0])
        except ValueError:
            return f'No user with username {self._params[0]} found!'    

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - removed user with username: {self._params[0]}')
        return msg       