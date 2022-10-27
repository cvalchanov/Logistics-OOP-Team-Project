import unittest
from src.models.constants.truck_availability import TruckAvailability
from src.models.truck import Truck

class TruckShould(unittest.TestCase):
    def test_init_setProperties(self):
        truck = Truck(1, 'Pesho', 10000, 15000, TruckAvailability.NO)

        self.assertEqual(1, truck.id)
        self.assertEqual('Pesho', truck.brand)
        self.assertEqual(10000, truck.capacity)
        self.assertEqual(15000, truck.range)
        self.assertEqual('no', truck.available)
        self.assertEqual(tuple(), truck.load)

    def test_truckAvailabilySetter(self):
        truck = Truck(1, 'Pesho', 10000, 15000, TruckAvailability.NO)

        truck.available = 'yes'

        self.assertEqual(TruckAvailability.YES, truck.available)

    def test_truckAvailabilitySetterRaisesErrorIfInvalid(self):
        truck = Truck(1, 'Pesho', 10000, 15000, TruckAvailability.YES)
        with self.assertRaises(ValueError):
            truck.available = 'Pesho'        

    def test_truck_info_returnsCorrectlyFormated(self):
        truck = Truck(1, 'Pesho', 10000, 15000, TruckAvailability.YES)

        expected = 'ID:1 - Pesho. Maximum capacity: 10000. Maximum Range: 15000. Availability: YES'

        self.assertEqual(expected, truck.info())

    def test_truck_str_returnsCorrectlyFormated(self):
        truck = Truck(1, 'Pesho', 10000, 15000, TruckAvailability.YES)

        expected = '1 Pesho 10000 15000 YES'

        self.assertEqual(expected, str(truck))
