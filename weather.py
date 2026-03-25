import requests

class City: 

    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):     
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=8dba48d7b350bdf531476b0f78866fef")

        except: 
            print("Unable to access the website")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In Chesapeak it is currently {self.temp} {units_symbol}")
        print(f"Todays high is {self.temp_max} {units_symbol}")
        print(f"Todays low is {self.temp_min} {units_symbol}")



gf_city = City("Chesapeak", lat=36.714, lon=-76.239)
gf_city.temp_print()

my_city = City("Denton", lat=33.215530, lon=-97.132446)
my_city.temp_print()
print(my_city.response_json)

