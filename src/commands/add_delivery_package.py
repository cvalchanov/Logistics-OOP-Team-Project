
from src.core.application_data import ApplicationData


class AddDeliveryPackageCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        self._params = params
        self._app_data = app_data
    
    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if len(self._params) != 3:
            return 'Invalid input'

        pack_id = int(self._params[0])
        route_id = self._params[2]
        truck_id = self._params[1]
    
        try:
            pack = self._app_data.find_unasigned_delivery_package(pack_id)
            if pack == None:
                return f'No package with id {pack_id} in unasigned delivery packages'
            truck = self._app_data.add_delivery_package(pack, truck_id, route_id)
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - Added pack #{pack_id} to truck #{truck.id}')
        except ValueError as err:
            # Truck add_package will raise exception if capacity exceeded.
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - Tried to add pack #{pack_id} to truck #{truck_id}: {err.args[0]}')
            return err.args[0]
        return f'Added pack #{pack_id} to truck #{truck.id}'
