from src.models.user import User
from src.core.application_data import ApplicationData
from src.models.constants.user_roles import UserRoles

class CreateUserCommand:
    def __init__(self, params: list[str], data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role != UserRoles.MANAGER:
            raise ValueError('Only managers can create new users')

        if len(self._params) != 6:
            raise ValueError('Invalid input')
        username = self._params[0].lower()
        password = self._params[1]
        first_name = self._params[2].capitalize()
        last_name = self._params[3].capitalize()
        phone = self._params[4]
        role = self._params[5]

        user = self._app_data.create_object_data(User, username, password, first_name, last_name, phone, role)

        try:
            isinstance(user, User)
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - created user: {user.username}')
            return f'User {user.username} created!'
        except ValueError as error:
            return error

