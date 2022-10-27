from datetime import datetime, timedelta
import unittest

from src.models.location import Location


class Constructor_Should(unittest.TestCase):
    def test_init_attributesValid(self):
        loc = Location('Melbourne', 'MEL', '2022-02-23', '06:00')

        self.assertEqual('2022-02-23', loc.date_in_location)
        self.assertEqual('06:00', loc.time_in_location)
    
    def test_init_attributes_inValid_raisesValueError(self):
        with self.assertRaises(ValueError):
            Location('Melbourne', 'MEL', '2022/02/23', '06/00')

class Methods_Should(unittest.TestCase):
    def test_init_is_in_progress_boolTrue(self):
        loc = Location('Melbourne', 'MEL', '2022-02-23', '06:00')

        bool_result = loc.is_in_progress()

        self.assertEqual(True, bool_result)
    
    def test_init_is_in_progress_boolFalse(self):
        loc_date = datetime.now().date()
        loc_time = (datetime.now() + timedelta(minutes=20)).time()
        loc = Location('Melbourne', 'MEL', loc_date, loc_time.strftime('%H:%M'))

        bool_result = loc.is_in_progress()

        self.assertEqual(False, bool_result)
    
    def test_str_format_valid(self):
        loc = Location('Melbourne', 'MEL', '2022-02-23', '6:00')

        str_loc = str(loc)

        self.assertEqual('Melbourne MEL 2022-02-23 6:00', str_loc)