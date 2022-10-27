import unittest
from src.models.constants.user_roles import UserRoles
from src.models.user import User

class UserShould(unittest.TestCase):
    def test_init_setsProperties(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        self.assertEqual('pesho1baby', user.username)
        self.assertEqual('admin1234', user.password)
        self.assertEqual('Pesho Peshov', user.name)
        self.assertEqual('911', user.phone)
        self.assertEqual('manager', user.user_role)

    def test_userPassword_setter_setsPasswordCorrectly(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        user.password = 'pesho'

        self.assertEqual('pesho', user.password)

    def test_userPassword_setter_raisesErrorIfInvalid(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        with self.assertRaises(ValueError):
            user.password = '!!!'

    def test_userPhone_setter_raisesErrorIfInvalid(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        with self.assertRaises(ValueError):
            user.phone = ''

    def test_userRole_setter_raisesErrorIfInvalid(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        with self.assertRaises(ValueError):
            user.user_role = 'Pesho'                        

    def test_userPhone_setter_setsPhoneCorrectly(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        user.phone = '112'

        self.assertEqual('112', user.phone)

    def test_userUserRole_setter_setsUserRoleCorrectly(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        user.user_role = 'employee'

        self.assertEqual(UserRoles.EMPLOYEE, user.user_role)

    def test_user_str_returnCorrectlyFormatted(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        expected = 'pesho1baby admin1234 Pesho Peshov 911 manager'

        self.assertEqual(expected, str(user))

    def test_user_info_returnCorrectlyFormatted(self):
        user = User('pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager')

        expected = 'Username: pesho1baby, Fullname: Pesho Peshov, Phone number: 911, Role: Manager'

        self.assertEqual(expected, user.info())        