from src.models.customer import Customer
from src.core.application_data import ApplicationData

class ViewAllCustomersCommand:
    def __init__(self, params, data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        msg = self._app_data.view_all_objects_data(Customer)
        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed all customers')
        return msg