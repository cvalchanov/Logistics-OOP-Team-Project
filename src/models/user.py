from os import path
from src.models.constants.user_roles import UserRoles
from src.core.data_files_manager import DataFilesManager

class User:
    def __init__(self, username: str, password: str, first_name: str, last_name: str, phone: str, user_role):
        if len(username) < 3 or len(username) > 15:
            raise ValueError('Username should be between 3 and 12 symbols')

        if not first_name and last_name:
            raise ValueError('User must have first and last name')

        self._username = username
        self.password = password
        self._name = first_name + ' ' + last_name
        self.phone = phone
        self.user_role = user_role

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def user_role(self):
        return self._user_role

    @password.setter
    def password(self, password:str):
        if len(password) < 4 or len(password) > 15:
            raise ValueError('Password should be between 4 and 15 symbols')
       
        if not all((ch.isalnum() or ch in '@-_*') for ch in password):
            raise ValueError('Invalid password symbols')
        
        self._password = password

    @phone.setter
    def phone(self, phone:str):
        if not phone:
            raise ValueError('User must have a phone')

        self._phone = phone

    @user_role.setter
    def user_role(self, role:str):
        if role.lower() == 'employee':
            self._user_role = UserRoles.EMPLOYEE
        elif role.lower() == 'supervisor':
            self._user_role = UserRoles.SUPERVISOR
        elif role.lower() == 'manager':
            self._user_role = UserRoles.MANAGER
        else:
            raise ValueError(f'User role must be {UserRoles.EMPLOYEE}, {UserRoles.SUPERVISOR} or {UserRoles.MANAGER}')

    def __str__(self):
        return f'{self.username} {self.password} {self.name} {self.phone} {self.user_role}'

    def info(self):
        return f'Username: {self.username}, Fullname: {self.name}, Phone number: {self.phone}, Role: {self.user_role.capitalize()}'