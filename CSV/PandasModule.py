import pandas

data = pandas.read_csv("weather_data.csv")

print(type(data))
print(type(data["temp"]))

### Print the entire Dataframe
print(data)

### Print the series
print(data["temp"])
print()

### Check the data type
print(data["temp"].dtypes)
print(data.dtypes)

#### Read the temp series data
temp_series = data["temp"]
print(temp_series)

#### Read the temp series data into a list
temp_list = data["temp"].to_list()
print(temp_list)
print(type(temp_list))

### Read the dataframe into dictionary
dict = data.to_dict()
print(dict)
print(type(dict))
