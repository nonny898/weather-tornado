import numpy
from geopy.distance import geodesic
 
# Weight = (WSPD) Wind Speed  * (WDIR) Wind Direction * (WDSD) Wind Deviation
 
stations = [{"station_1": []}, {"station_2": []}]
# ("Lat", "Long")
stationX = ["station", "weight"]
 
matrixOfStations = []
def applyDirection(nswe=1):
   for station in stations:
       weight = 0
       if wind_direction in numpy.arange(45.0..135.0):
           weight = (station["RAIN"] * 1) / station["WSPD"] * station["WDSD"]
       elif wind_direction in numpy.arange(225.0..315.0):
           weight=  (station["RAIN"] * -1) / station["WSPD"] * station["WDSD"]
       matrixOfStations.append( {"lat": station["lat"], "lon": station["lon"], "weight": weight})
 
def applyIntersectionSum(list):
   distance = []
 
   for x in range(0..list__len__()-1)
       for j in range(0..list__len__()-1)
           if x not j:
               station_a = (x["lat"], x["lon"])
               station_b = (j["lat"], j["lon"])
               distanceBetweenTowStation = geodesic(station_a, station_b).meteres
               distanceBetweenTowStation <= 10
              

