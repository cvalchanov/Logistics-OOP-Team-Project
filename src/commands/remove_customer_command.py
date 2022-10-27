from src.models.customer import Customer
from src.core.application_data import ApplicationData
from src.models.constants.user_roles import UserRoles

class RemoveCustomerCommand:
    def __init__(self, params, data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role == UserRoles.EMPLOYEE:
            raise ValueError('Employees can\'t remove customers')

        if len(self._params) != 1:
            raise ValueError('Indaliv Input')

        try:
            msg = self._app_data.remove_object_data(Customer, self._params[0])
        except ValueError:
            return f'No customer with ID {self._params[0]} found!'    

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - removed customer with ID: {self._params[0]}')
        return msg        