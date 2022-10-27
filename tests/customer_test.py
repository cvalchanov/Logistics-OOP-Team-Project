import unittest
from src.models.customer import Customer

class CustomerShould(unittest.TestCase):
    def test_init_setProperties(self):
        customer = Customer(1, 'Pesho', 'Peshov', '0000', '')

        self.assertEqual(1, customer.id)
        self.assertEqual('Pesho Peshov', customer.name)
        self.assertEqual('0000', customer.phone)
        self.assertEqual('', customer.email)

    def test_init_raisesErrorWithInvalidFirstName(self):

        with self.assertRaises(ValueError):
            customer = Customer(1, '', 'Peshov', '0000', '')

    def test_init_raisesErrorWithInvalidLastName(self):
        with self.assertRaises(ValueError):
            customer = Customer(1, 'Pesho', '', '0000', '')

    def test_customerPhone_setter_raisesErrorIfInvalid(self):
        customer = Customer(1, 'Pesho', 'Peshov', '0000', '')

        with self.assertRaises(ValueError):
            customer.phone = ''

    def test_customerEmailSetterWorks(self):
        customer = Customer(1, 'Pesho', 'Peshov', '0000', '')

        customer.email = 'abc@abv.bg'

        self.assertEqual('abc@abv.bg', customer.email)

    def test_customer_str_returnsCorrectlyFormatted(self):
        customer = Customer(1, 'Pesho', 'Peshov', '0000', 'abc@abv.bg')

        expected = '1 Pesho Peshov 0000 abc@abv.bg'

        self.assertEqual(expected, str(customer))

    def test_customer_info_returnsCorrectlyFormatted(self):
        customer = Customer(1, 'Pesho', 'Peshov', '0000', 'abc@abv.bg')

        expected = 'ID:1. Name: Pesho Peshov. Phone number: 0000. Email: abc@abv.bg'

        self.assertEqual(expected, customer.info())
