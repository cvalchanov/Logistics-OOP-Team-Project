from datetime import datetime, timedelta
from os import path

from src.models.location import Location


class LocationFactory:
    SPEED = 87
    ABRIVIATIONS = {
        'SYD': 'Sydney', 
        'MEL': 'Melbourne', 
        'ADL': 'Adelaide', 
        'ASP': 'Alice Springs', 
        'BRI': 'Brisban', 
        'DAR': 'Darwin', 
        'PER': 'Perth'
        }

    @classmethod
    def find_city_names(cls, city):
        for k,v in cls.ABRIVIATIONS.items():
            if k == city:
                return v
    
    @classmethod
    def calculate_location_time(cls, start_time: datetime, distance):
        # Oct 12th 06:00
        in_hours = round(distance / cls.SPEED)
        days = in_hours // 24
        hours = in_hours % 24
        mins = 0
        new_date_time = start_time + timedelta(days=days, hours=hours, minutes=mins)

        return new_date_time

    @classmethod
    def calculate_distances(cls, cities, file_lines, first_is_zero = False):
        results = []
        if first_is_zero:
            results.append(0)
        
        col = file_lines[0].split()

        for city_index in range(len(cities) - 1):
            idx = col.index(cities[city_index + 1])
            dist = cls.check_line(cities[city_index], file_lines, idx)
            results.append(int(dist))
        
        return results

    @classmethod
    def check_line(cls, city, file_lines, idx):
        for line in range(1, len(file_lines)):
            if file_lines[line] and city in file_lines[line]:
                content = file_lines[line].split()
                dist = content[idx]
                return dist

    @classmethod
    def create_location_by_abrreviation(cls, city, date, time):
        name = LocationFactory.find_city_names(city)
        loc = Location(name, city, date, time)
        return loc
