from datetime import datetime


class Location:
    def __init__(self, city, abbreviation, date_in_location, time_in_location) -> None:
        self._city = city
        self._abbreviation = abbreviation
        self._date_in_location = date_in_location
        self._time_in_location = time_in_location
        self._date_time = datetime.strptime(f'{self._date_in_location} {self._time_in_location}', '%Y-%m-%d %H:%M')
    
    @property
    def time_in_location(self):
        return self._time_in_location

    @property
    def date_in_location(self):
        return self._date_in_location

    @property
    def abbreviation(self):
        return self._abbreviation

    def is_in_progress(self):
        if datetime.now() > self._date_time:
            return True
        return False
    
    def __str__(self) -> str:
        output = f'{self._city} {self._abbreviation} {self._date_in_location} {self._time_in_location}'
        return output
    
    def info(self):
        output = f'{self._city} ({self._date_in_location} {self._time_in_location})'
        return output
