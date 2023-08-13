import csv
import pandas

##### manual Efforts
file = open("weather_data.csv",mode="r")
content = file.readlines()

for i in content:
  stripped_content = i.strip()
  print(stripped_content)

##### using csv
with open("weather_data.csv") as data_file:
  data = csv.reader(data_file)
  skip_heading = True
  temperatures = []
  for row in data:
    if skip_heading:
      skip_heading = False
    else:
      temperatures.append(int(row[1]))
      print(int(row[1]))

  print(temperatures)

##### Using Pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
