import math
import requests

tau = "אוניברסיטת תל אביב"

class User:
    def __init__(self, address, ID, mail, birth_year):
        self.ID = ID
        self.address = address
        self.mail = mail
        self.birth_year = birth_year
        self.organizations = []
        self.mydrives = []

    def ask_for_ride(self, day, start, end, address):
        assert start <= end
        options = []
        while start <= end:
            drives = Drive.drives[day][start]
            for drive in drives:
                extra = Drive.calc_extra(drive, address)
                if extra <= drive.max_time_add:
                    options.append((drive, extra))
            start += 15
        return sorted(options, key=lambda x: x[1])

    def create_drive(self, arrive_time, day, max_extra):
        drive = Drive(self, arrive_time, day, 2, max_extra, self.address)
        self.mydrives.append(drive)


class Drive:
    drives = [{} for i in range(7)]

    def __init__(self, user, arrive_time, day, driver, max_time_add, address):
        self.arrive_time = arrive_time
        self.day = day
        self.driver = driver
        self.trempistim = []
        self.address = address
        self.max_time_add = max_time_add
        self.duration = get_travel_time(self.address,tau)
        if arrive_time not in Drive.drives[day] == None:
            Drive.drives[day][arrive_time] = []
        Drive.drives[day][arrive_time].append(self)

    @staticmethod
    def calc_extra(trempist_address):
        new_time = get_travel_time(self.address, trempist_address) + get_travel_time(trempist_address, tau)
        return new_time - self.arrive_time


def get_travel_time(origin, destination, mode='driving'):
    api_key = 'AIzaSyCfZUFEceP68o8cF06J0gVYoZraZ5ET9bw'  # Replace with your Google Maps API key
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    params = {
        'origins': origin,
        'destinations': destination,
        'mode': mode,
        'key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        duration_sec = data['rows'][0]['elements'][0]['duration']['value']
        return math.floor(duration_sec / 60)
    else:
        print('Error occurred.')
        return None


user1 = User("אבא הלל 68 רמת גן", 207105214, "avivyossef@mail.tau.ac.il", 1999)
user2 = User("ביאליק 50 רמת גן", 207105213, "nadav@mail.tau.ac.il", 1999)
user3 = User("גיסין 50 פתח תקווה", 207105213, "nadav@mail.tau.ac.il", 1999)
print(Drive.drives)
user1.create_drive(300, 2, 60)
user3.create_drive(300, 2, 60)
print(Drive.drives[2])
print(user2.ask_for_ride(2, 300,300, user2.address))
