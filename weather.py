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
    result = []
    with open('201908132355.mdf') as csvfile:
        read = csv.reader(csvfile, delimiter=' ')
        next(read, None)
        for row in read:
            row = list(filter(None, row))
            data = {
                'name': row[0],
                'speed': row[5],
                'direction': row[7],
                'deviation': row[8]
            }
            result.append(data)
    return result


def main():
    stations = location()
    print(stations)
    mdf = readmdf()
    fullStationList = []
    for STID in stations:
        for station in stations[STID].:
            data = {'name': station[2], 'latitude': station[0], 'longitude': station[1]}
            stationData = {station[2]: data}
            fullStationList.append(stationData)
    print(fullStationList)
    # for station in mdf:
    #     print(station['name'])

if __name__ == '__main__':
    main()
