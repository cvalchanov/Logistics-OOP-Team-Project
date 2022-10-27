import unittest
from src.models.delivery_package import DeliveryPackage


class Constructor_Should(unittest.TestCase):
    def test_init_attributes(self):
        # Arrange & Act
        pack = DeliveryPackage(1, 45, 1, 'MEL', 'SYD')

        # Assert
        self.assertEqual(1, pack.id)
        self.assertEqual(45, pack.weight)

class AddArrivalDateTime_Should(unittest.TestCase):
    def test_create_arrival_date_and_time(self):
        # Arrange
        pack = DeliveryPackage(1, 45, 1, 'MEL', 'SYD')

        # Act
        pack.add_arrival_date_time('2022-2-23', '6:30')

        # Assert
        self.assertEqual('2022-2-23 6:30', pack.arrival_date_time)

class Info_Str_Should(unittest.TestCase):
    def test_create_correct_text_arrivalDateTime(self):
        # Arrange
        pack = DeliveryPackage(1, 45, 1, 'MEL', 'SYD')
        pack.add_arrival_date_time('2022-2-23', '6:30')

        # Act
        txt = pack.info()

        # Assert
        self.assertEqual(txt, 'Delivery Package ID: 1 Weight: 45 Customer_ID: 1 Departure: MEL Arrival: SYD Arrival Time: 2022-2-23 6:30')

    def test_create_correct_text_noArrivalDateTime(self):
        # Arrange
        pack = DeliveryPackage(1, 45, 1, 'MEL', 'SYD')

        # Act
        txt = pack.info()

        # Assert
        self.assertEqual(txt, 'Delivery Package ID: 1 Weight: 45 Customer_ID: 1 Departure: MEL Arrival: SYD')

    def test_create_correct_str_arrivalDateTime(self):
         # Arrange
        pack = DeliveryPackage(1, 45, 1, 'MEL', 'SYD')
        pack.add_arrival_date_time('2022-2-23', '6:30')

        # Act
        txt = str(pack)

        # Assert
        self.assertEqual(txt, '1 45 1 MEL SYD 2022-2-23 6:30')

    def test_create_correct_str_noArrivalDateTime(self):
         # Arrange
        pack = DeliveryPackage(1, 45, 1, 'MEL', 'SYD')

        # Act
        txt = str(pack)

        # Assert
        self.assertEqual(txt, '1 45 1 MEL SYD')
