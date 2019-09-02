import csv
import numpy
from geopy.distance import geodesic


def location():
    loc = {'loc': []}
    with open('geoinfo.csv') as geofile:
        readGeo = csv.reader(geofile, delimiter=',')
        next(readGeo, None)
        for row in readGeo:
            name = row[1]
            latitude = float(row[7])
            longitude = float(row[8])
            loc['loc'].append([latitude, longitude, name])
        return loc


def template():
    dictionary = {}
    minute = 0.0
    for row in range(576):
        dictionary[minute] = [minute]
        minute += 5.0
    return dictionary


def readcsv():
    tempName = ['hoba', 'holl', 'mang']
    result = []
    for name in tempName:
        tempList = []
        with open('20190813' + name + '.mts') as csvfile:
            read = csv.reader(csvfile, delimiter=' ')
            next(read, None)
            for row in read:
                row = list(filter(None, row))
                tempList.append(row)
            result.append(tempList)
    return result


def pressure():
    temp = template()
    csvinput = readcsv()
    for station in csvinput:
        minute = 0.0
        for row in station:
            measurements = float(row[12])
            if minute <= 1435:
                temp[int(row[2])].append(measurements)
            else:
                temp[int(row[2]) + 1440].append(measurements)
            minute += 5.0
    return temp


def temperature():
    temp = template()
    csvinput = readcsv()
    for station in csvinput:
        minute = 0.0
        for row in station:
            measurements = float(row[4])
            if minute <= 1435:
                temp[int(row[2])].append(measurements)
            else:
                temp[int(row[2]) + 1440].append(measurements)
            minute += 5.0
    return temp


def speed():
    temp = template()
    csvinput = readcsv()
    for station in csvinput:
        minute = 0.0
        for row in station:
            measurements = float(row[5])
            if minute <= 1435:
                temp[int(row[2])].append(measurements)
            else:
                temp[int(row[2]) + 1440].append(measurements)
            minute += 5.0
    return temp


def precipitation():
    temp = template()
    csvinput = readcsv()
    for station in csvinput:
        minute = 0.0
        for row in station:
            measurements = float(row[11])
            if minute <= 1435:
                temp[int(row[2])].append(measurements)
            else:
                temp[int(row[2]) + 1440].append(measurements)
            minute += 5.0
    return temp


def readmdf():
    data = {}
    with open('201908132355.mdf') as csvfile:
        read = csv.reader(csvfile, delimiter=' ')
        next(read, None)
        for row in read:
            row = list(filter(None, row))
            data[row[0]] = {
                'speed': float(row[5]),
                'direction': int(row[7]),
                'deviation': float(row[8]),
                'rain': float(row[11])
                }
    return data


def createdict():
    stations = location()
    resultDict = readmdf()
    for STID in stations:
        for station in stations[STID]:
            if station[2] in resultDict:
                resultDict[station[2]].update({
                    'latitude': float(station[0]),
                    'longitude': float(station[1])
                })
    return resultDict


def applydirection():
    stationDict = createdict()
    for station in stationDict:
        wind_direction = stationDict[station]['direction']
        rain_station = stationDict[station]['rain']
        wind_speed = stationDict[station]['speed']
        wind_deviation = stationDict[station]['deviation']
        weight = 0
        if wind_direction in numpy.arange(45.0,135.0):
            weight = (rain_station * 1) / wind_speed * wind_deviation
        elif wind_direction in numpy.arange(225.0,315.0):
            weight = (rain_station * -1) / wind_speed * wind_deviation
        stationDict[station].update({'weight': weight})
    return stationDict


def applyintersectionsum():
    data = applydirection()
    stationsDistanceList = []
    for main_station in data:
        for compare_station in data:
            if main_station is not compare_station:
                main_latlong = (
                    data[main_station]['latitude'],
                    data[main_station]['longitude']
                )
                compare_latlong = (
                    data[compare_station]['latitude'],
                    data[compare_station]['longitude']
                )
                distanceBetween = geodesic(main_latlong,compare_latlong).kilometers
                if distanceBetween not in stationsDistanceList:
                    stationsDistanceList.append(distanceBetween)


def timelist():
    minute = 0
    hour = 0
    lst = []
    for i in range(0,1436,5):
        if minute > 55:
            hour += 1
            minute = 0
        lst.append(str('{:02d}'.format(hour)) + str('{:02d}'.format(minute)))
        minute += 5
    return lst


def main():
    print(timelist())


if __name__ == '__main__':
    main()
