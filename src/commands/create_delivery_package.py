
from src.core.factories.id_factory import IDFactory
from src.core.application_data import ApplicationData


class CreateDeliveryPackageCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        self._params = params
        self._app_data = app_data
    
    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if len(self._params) != 4:
            return 'Invalid input'

        weight, customer_id, start_locion, end_location = self._params
        id = IDFactory.get_package_id()
        self._app_data.create_delivery_package(id, weight, customer_id, start_locion, end_location)

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - created pack {id}')
        return f'Created pack {id}'
