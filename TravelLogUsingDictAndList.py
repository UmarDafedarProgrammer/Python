travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,NumOfVisits,CityList):
    # travel_log.append(
    #     {
    #         "country":country,
    #         "visits": NumOfVisits,
    #         "cities": CityList
    #     })
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = NumOfVisits
  new_country["cities"] = CityList
  travel_log.append(new_country)
  



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
