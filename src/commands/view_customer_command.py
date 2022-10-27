from src.models.customer import Customer
from src.core.application_data import ApplicationData

class ViewCustomerCommand:
    def __init__(self, params, data: ApplicationData):
        self._app_data = data
        self._params = params

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        customer_id = self._params[0]
        try:
            customer = self._app_data.find_data_by_value(Customer, customer_id)
        except ValueError:
            return f'No customer with ID {customer_id} found!'

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed customer with ID: {customer_id}')
        return customer.info()
