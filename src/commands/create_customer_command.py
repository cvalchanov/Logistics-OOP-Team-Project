from src.core.constants.common_constants import CommonConstants
from src.core.factories.id_factory import IDFactory
from src.models.customer import Customer
from src.core.application_data import ApplicationData

class CreateCustomerCommand:
    def __init__(self, params: list[str], data: ApplicationData):
        self._params = params
        self._app_data = data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if len(self._params) < 3 or len(self._params) > 4:
            raise ValueError('Invalid input')
        
        id = IDFactory.get_customer_id()
        first_name = self._params[0].capitalize()
        last_name = self._params[1].capitalize()
        phone = self._params[2]
        if len(self._params) > 3:
            email = self._params[3]
        else:
            email = CommonConstants.NOT_AVAILABLE
        customer = self._app_data.create_object_data(Customer, id, first_name, last_name, phone, email)

        try:
            isinstance(customer, Customer)
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - created customer with ID:{customer.id}')
            return f'Created customer with ID:{customer.id}'
        except ValueError as error:
            return error