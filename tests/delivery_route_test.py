import unittest
from unittest.mock import Mock

from src.models.delivery_route import DeliveryRoute


class Constructor_Should(unittest.TestCase):
    def test_init_attributesValid(self):
        # Arrange & Act
        route = DeliveryRoute(1, 877, 'N/A', ['Melbourne MEL 2022-02-23 06:00', 'Sydney SYD 2022-02-23 16:00'], '2022-02-23', '16:00')

        # Assert
        self.assertEqual(1, route.id)
        self.assertEqual('2022-02-23', route.arrival_date)
        self.assertEqual('16:00', route.arrival_time)
    
    def test_init_attributesWith_get_truck_id_valid(self):
        fake_truck = Mock()
        fake_truck.id = 1

        # Act
        route = DeliveryRoute(1, 877, fake_truck, ['Melbourne MEL 2022-02-23 06:00', 'Sydney SYD 2022-02-23 16:00'], '2022-02-23', '16:00')

        self.assertEqual(1, route.get_truck_id())
    
    def test_init_raises_locations_length_ValueError(self):
        # Arrange
        locs = [Mock()]

        # Act & Assert
        with self.assertRaises(ValueError):
            DeliveryRoute(1, 877, 'N/A', locs, '2022-02-23', '16:00')
    
class Methods_Should(unittest.TestCase):
    def test_is_in_progress_returnBoolValid(self):
        # Arrange
        fake_loc_method = Mock(return_value=True)
        route = DeliveryRoute(1, 877, 'N/A', [fake_loc_method, fake_loc_method], '2022-02-23', '16:00')
        
        # Act
        bool_value = route.is_in_progress()

        # Assert
        self.assertEqual(True, bool_value)
    
    def test_find_package_in_truck_valid(self):
        # Arrange
        fake_pack = Mock()
        fake_pack.id = 1
        fake_truck = Mock()
        fake_truck.load = [fake_pack]

        # Act
        route = DeliveryRoute(1, 877, fake_truck, ['Melbourne MEL 2022-02-23 06:00', 'Sydney SYD 2022-02-23 16:00'], '2022-02-23', '16:00')
        pack = route.find_package_in_truck(1)

        # Assert
        self.assertEqual(fake_pack, pack)

    def test_find_package_in_truck_doNothingWhenNoPack(self):
        # Arrange
        fake_pack = Mock()
        fake_pack.id = 1
        fake_truck = Mock()
        fake_truck.load = [fake_pack]

        # Act
        route = DeliveryRoute(1, 877, fake_truck, ['Melbourne MEL 2022-02-23 06:00', 'Sydney SYD 2022-02-23 16:00'], '2022-02-23', '16:00')
        pack = route.find_package_in_truck(2)

        # Assert
        self.assertEqual(None, pack)

    def test_find_current_stop_valid(self):
        # Arrange
        fake_loc_method_1 = Mock(return_value=True)
        loc_1 = Mock()
        loc_1.is_in_progress = fake_loc_method_1
        fake_loc_method_2 = Mock(return_value=False)
        loc_2 = Mock()
        loc_2.is_in_progress = fake_loc_method_2
        route = DeliveryRoute(1, 877, 'N/A', [loc_1, loc_2], '2022-02-23', '16:00')

        #Act
        loc = route.find_current_stop()

        # Assert
        self.assertEqual(loc_1, loc)

    def test_find_current_stop_inValid(self):
        # Arrange
        fake_loc_method_1 = Mock(return_value=False)
        loc_1 = Mock()
        loc_1.is_in_progress = fake_loc_method_1
        fake_loc_method_2 = Mock(return_value=False)
        loc_2 = Mock()
        loc_2.is_in_progress = fake_loc_method_2
        route = DeliveryRoute(1, 877, 'N/A', [loc_1, loc_2], '2022-02-23', '16:00')

        #Act
        loc = route.find_current_stop()

        # Assert
        self.assertEqual(None, loc)
    

