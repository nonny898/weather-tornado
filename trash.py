# fig = plt.figure()
# names = []
# stationIDs = []
# stationNumbers = []
# with open('geoinfo.csv') as geofile:
#     readGeo = csv.reader(geofile, delimiter=',')
#     next(readGeo, None)
#     for row in readGeo:
#         number = row[0]
#         ID = row[1]
#         station = row[2]
#
#         names.append(station)
#         stationNumbers.append(int(number))
#         stationIDs.append('20190814'+ID.lower())


# data[name] = [times, speeds, temperatures, rains, pressures]
# return data
# averageTemperature = np.average(temperatures)
# averageSpeed = np.average(speeds)
# maxPressure = np.max(pressures)
# minPressure = np.min(pressures)
# averagePrecipitation = np.average(precipitation)

# print(averageTemperature)
# print(averageSpeed)
# print(maxPressure)
# print(minPressure)
# print(averagePrecipitation)
# print()

# plt.figure(figsize=(10, 10))
# axPressure = plt.subplot(4, 1, 1)
# axPressure.set_title("Pressure")
# axPressure.set_ylabel('Pressure (mb)')
# axPressure.set_xlabel('Time (minutes)')
#
# axTemperature = plt.subplot(4, 1, 2)
# axTemperature.set_title('Temperature')
# axTemperature.set_ylabel('Temperature (Celsius)')
# axTemperature.set_xlabel('Time (minutes)')
#
# axSpeed = plt.subplot(4, 1, 3)
# axSpeed.set_title('Speed')
# axSpeed.set_ylabel('Speed (mps')
# axSpeed.set_xlabel('Time (minutes)')
#
# axRain = plt.subplot(4, 1, 4)
# axRain.set_title('Rain')
# axRain.set_ylabel('Precipitation (millimeters)')
# axRain.set_xlabel('Time (minutes)')
#

# colorAs = {
#     'hoba': "red",
#     'holl': "green",
#     'mang': "blue"
# }
# fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.02)
#
# for station in tempName:
#     timesNp = np.array(data[station][0])
#     speedNp = np.array(data[station][1])
#     temperatureNp = np.array(data[station][2])
#     rainsNp = np.array(data[station][3])
#     pressuresNp = np.array(data[station][4])
#
#     fig.add_trace(go.Scatter(
#         x=data[station][0],
#         y=data[station][1],
#         name=station+" speed",
#         line=dict(color=colorAs[station]
#                   )),
#         row=1,
#         col=1)
#
#     peaks, _ = find_peaks(speedNp, height=0)
#     fig.add_trace(go.Scatter(
#         x=timesNp[peaks],
#         y=speedNp[peaks],
#         mode='markers',
#         marker=dict(size=4,
#                     color='red',
#                     symbol='cross'),
#         name='Detected Speed Peaks'),
#         row=1,
#         col=1)
#
#     fig.add_trace(go.Scatter(
#         x=data[station][0],
#         y=data[station][2],
#         name=station+" temperature",
#         line=dict(color=colorAs[station]
#                   )),
#         row=2,
#         col=1)
#
#     peaks, _ = find_peaks(temperatureNp, height=0)
#     fig.add_trace(go.Scatter(
#         x=timesNp[peaks],
#         y=temperatureNp[peaks],
#         mode='markers',
#         marker=dict(size=4,
#                     color='red',
#                     symbol='cross'),
#         name='Detected Temperature Peaks'),
#         row=2,
#         col=1)
#
#     fig.add_trace(go.Scatter(
#         x=data[station][0],
#         y=data[station][3],
#         name=station+" rain",
#         line=dict(color=colorAs[station]
#                   )),
#         row=3,
#         col=1)
#
#     peaks, _ = find_peaks(rainsNp, height=0)
#     fig.add_trace(go.Scatter(
#         x=timesNp[peaks],
#         y=rainsNp[peaks],
#         mode='markers',
#         marker=dict(size=4,
#                     color='red',
#                     symbol='cross'),
#         name='Detected Rain Peaks'),
#         row=3,
#         col=1)
#
#     fig.add_trace(go.Scatter(
#         x=data[station][0],
#         y=data[station][4],
#         name=station+" pressure",
#         line=dict(color=colorAs[station]
#                   )),
#         row=4,
#         col=1)
#
#     peaks, _ = find_peaks(pressuresNp, height=0)
#     fig.add_trace(go.Scatter(
#         x=timesNp[peaks],
#         y=pressuresNp[peaks],
#         mode='markers',
#         marker=dict(size=4,
#                     color='red',
#                     symbol='cross'),
#         name='Detected  Pressure Peaks'),
#         row=4,
#         col=1)
#
# fig.show()
#     timesNp = np.array(data[name][0])
#     speedNp = np.array(data[name][1])
#     temperatureNp = np.array(data[name][2])
#     rainsNp = np.array(data[name][3])
#     pressuresNp = np.array(data[name][4])
#
#     peaks, _ = find_peaks(pressuresNp, height=0)
#     axPressure.plot(timesNp, pressuresNp, label=name)
#     axPressure.plot(timesNp[peaks], pressuresNp[peaks], "x")
#     axPressure.legend(loc='lower left')
#
#     peaks, _ = find_peaks(temperatureNp, height=0)
#     axTemperature.plot(timesNp, temperatureNp, label=name)
#     axTemperature.plot(timesNp[peaks], temperatureNp[peaks], "x")
#     axTemperature.legend(loc='lower left')
#
#     peaks, _ = find_peaks(speedNp, height=0)
#     axSpeed.plot(timesNp, speedNp, label=name)
#     axSpeed.plot(timesNp[peaks], speedNp[peaks], "x")
#     axSpeed.legend(loc='lower left')
#
#     peaks, _ = find_peaks(rainsNp, height=0)
#     axRain.plot(timesNp, rainsNp, label=name)
#     axRain.plot(timesNp[peaks], rainsNp[peaks], "x")
#     axRain.legend(loc='lower left')
#
# plt.show()