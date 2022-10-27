from src.core.application_data import ApplicationData


class AddDeliveryPackageBulkCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        self._app_data = app_data
        self._params = params

    def execute(self):
        truck_id, route_id, *pack_ids = self._params
        
        for pack_id in pack_ids:
            pack = self._app_data.find_unasigned_delivery_package(int(pack_id))
            self._app_data.add_delivery_package(pack, truck_id, route_id)
         
        packs = ', '.join([f'#{x}' for x in pack_ids])

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - added packs {packs} to truck #{truck_id}')
        return f'Added packs {packs} to truck #{truck_id}'
