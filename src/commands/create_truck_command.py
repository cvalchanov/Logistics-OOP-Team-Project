from src.core.factories.id_factory import IDFactory
from src.models.truck import Truck
from src.core.application_data import ApplicationData
from src.models.constants.truck_availability import TruckAvailability
from src.models.constants.user_roles import UserRoles

class CreateTruckCommand:
    def __init__(self, params: list[str], data: ApplicationData):
        self._params = params
        self._app_data = data   

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role != UserRoles.MANAGER:
            raise ValueError('Only managers can create new trucks')

        if len(self._params) < 3 or len(self._params) > 4:
            raise ValueError('Invalid input')

        if len(self._params[0]) < 2 or len(self._params[0]) > 15:
            raise ValueError('Truck brand must be between 2 and 15 symbols')

        if int(self._params[1]) < 0:
            raise ValueError('Truck capacity must be positive')

        if int(self._params[2]) < 0:
            raise ValueError('Truck maximum range must be positive')

        brand = self._params[0].capitalize()
        capacity = int(self._params[1])
        range = int(self._params[2])
        
        if len(self._params) > 3:
            if self._params[3].lower() == 'yes':
                availability = TruckAvailability.YES
            elif self._params[3].lower() == 'no':
                availability = TruckAvailability.NO
            else:
                raise ValueError(f'Truck availability can be only {TruckAvailability.YES} or {TruckAvailability.NO}')
        else:
            availability = TruckAvailability.YES
        id = IDFactory.get_truck_id()
        truck = self._app_data.create_truck(id, brand, capacity, range, availability)


        try:
            isinstance(truck, Truck)
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - created truck with ID:{truck.id}')
            return f'Created truck with ID:{truck.id}'
        except ValueError as error:
            return error
        

    