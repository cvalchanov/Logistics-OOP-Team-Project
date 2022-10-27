class Customer:
    def __init__(self, customer_id, first_name, last_name, phone, email):
        self._customer_id = customer_id

        if not first_name:
            raise ValueError('Customer name cannot be empty')

        if not last_name:
            raise ValueError('Customer name cannot be empty')

        self._name = first_name + ' ' + last_name

        if not phone:
            raise ValueError('Customer phone number cannot be empty')

        self.phone = phone
        self.email = email

    @property
    def id(self):
        return self._customer_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValueError('Customer phone number cannot be empty')
        self._phone = value        


    def __str__(self):
        return f'{self.id} {self.name} {self.phone} {self.email}'

    def info(self):
        return f'ID:{self.id}. Name: {self.name}. Phone number: {self.phone}. Email: {self.email}'


        