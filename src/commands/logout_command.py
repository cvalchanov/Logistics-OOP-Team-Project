from src.core.application_data import ApplicationData

class LogoutCommand:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You are not logged in')

        logged_user = self._app_data.logged_user
        msg = self._app_data.user_logout()
        self._app_data.update_log(f' - {logged_user.username} - logged out successfully')
        return msg
