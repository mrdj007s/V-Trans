from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator=Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
)

def calculateDistance(loc1,loc2):
    locationinfo=geolocator.geocode(loc1)
    cor1=(float(locationinfo.latitude),float(locationinfo.logitude))

    locationinfo2=geolocator.geocode(loc2)
    cor2=(float(locationinfo2.latitude),float(locationinfo2.logitude))

    print(geodesic(cor1,cor2).kilometers)

loc1=input("Enter First address:")
loc2=input("Enter Second address:")

calculateDistance(loc1,loc2)