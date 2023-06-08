import json

drives = [
    {
        "arrive_time": "08:00",
        "day": 0,
        "driver": "John",
        "max_time_add": 30,
        "address": "10 Einstein St, Tel Aviv"
    },
    {
        "arrive_time": "09:15",
        "day": 0,
        "driver": "Alice",
        "max_time_add": 45,
        "address": "15 Herzl St, Tel Aviv"
    },
    {
        "arrive_time": "07:45",
        "day": 1,
        "driver": "Mike",
        "max_time_add": 20,
        "address": "5 Rothschild Blvd, Tel Aviv"
    },
    {
        "arrive_time": "08:30",
        "day": 2,
        "driver": "Sarah",
        "max_time_add": 25,
        "address": "20 Dizengoff St, Tel Aviv"
    },
    {
        "arrive_time": "07:15",
        "day": 3,
        "driver": "David",
        "max_time_add": 35,
        "address": "12 Ben Yehuda St, Tel Aviv"
    },
    {
        "arrive_time": "09:45",
        "day": 4,
        "driver": "Emily",
        "max_time_add": 40,
        "address": "25 Allenby St, Tel Aviv"
    },
    {
        "arrive_time": "07:30",
        "day": 0,
        "driver": "Tom",
        "max_time_add": 30,
        "address": "8 Ibn Gabirol St, Tel Aviv"
    },
    {
        "arrive_time": "08:15",
        "day": 1,
        "driver": "Olivia",
        "max_time_add": 35,
        "address": "30 King George St, Tel Aviv"
    },
    {
        "arrive_time": "09:00",
        "day": 2,
        "driver": "James",
        "max_time_add": 20,
        "address": "18 HaYarkon St, Tel Aviv"
    },
    {
        "arrive_time": "07:45",
        "day": 3,
        "driver": "Emma",
        "max_time_add": 25,
        "address": "22 Allenby St, Tel Aviv"
    }
]

data = {"drives": drives}

# Save the JSON data to a file
with open('drives.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
