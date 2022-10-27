class DeliveryPackage:
    def __init__(self, id, weight, customer_id, start_locion, end_location) -> None:
        self._id = id
        self._weight = int(weight)
        self._customer_id = customer_id
        self._start_location = start_locion
        self._end_location = end_location
        self._arrival_date_time = None
    
    @property
    def id(self):
        return self._id
    
    @property
    def arrival_date_time(self):
        return self._arrival_date_time
    
    @property
    def weight(self):
        return self._weight
    
    def add_arrival_date_time(self, arrival_date, arrival_time):
        self._arrival_date_time = f'{arrival_date} {arrival_time}'

    def __str__(self) -> str:
        output = f'{self._id} {self._weight} {self._customer_id} {self._start_location} {self._end_location}'
        if self._arrival_date_time != None:
            output = f'{output} {self._arrival_date_time}'
        return output

    def info(self):
        output = f'Delivery Package ID: {self._id} Weight: {self._weight} Customer_ID: {self._customer_id} Departure: {self._start_location} Arrival: {self._end_location}'
        if self._arrival_date_time != None:
            output = f'{output} Arrival Time: {self._arrival_date_time}'
        return output
