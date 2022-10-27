from src.core.application_data import ApplicationData

class LoginCommand:
    def __init__(self, params, data: ApplicationData):
        self._params = params
        self._app_data = data
    
    def execute(self):
        if self._app_data.logged_user != None:
            raise ValueError('You need to log out first')

        if len(self._params) != 2:
            raise ValueError('Invalid input')

        try:
            msg = self._app_data.user_login(self._params)
        except ValueError:
            return f'Wrong username'

        if msg != 'Wrong password':
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - logged in successfully')
        
        return msg


        
