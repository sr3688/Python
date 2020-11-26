travel_log=[]

def add_new_cities(country,times_visited,cities):
    info={}
    info["country"]=country
    info["visited"]=times_visited
    info["cities"]=cities
    travel_log.append(info)
        
add_new_cities("France",12,["Paris","Lillie","Dijon"])
add_new_cities("Germany",11,["Berlin","Hamburg","Stuttgard"])
add_new_cities("Russia",2,["Moscow","Saint Petersburg","Sochi"])

print(travel_log)
        

