


# for sim related information

import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number=input("Enter Your Number With +__ : ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print("Phone No :  ", phone)
print("TimeZone : ", time)
print("Carrier  : ", car)

# for lattitude and longotude

import opencage
from opencage.geocoder import OpenCageGeocode
key= '3e536a00a8df400da86f0720e5a2d90b'
geocoder = OpenCageGeocode(key)
query = str(reg)
results = geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print("Lattitude And Longitude : ", lat,", ", lng)


# for loaction in map
import folium
myMap= folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], ppopup=reg).add_to(myMap)
myMap.save("PhoneNumberLocation.html")