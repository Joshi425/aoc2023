from pprint import pprint
f = open("Input.txt", "r")

# def map_value(maps,value):
#     for map in maps:
#         for i in range(map["source_range_start"],map["source_range_start"]+map["range_length"]):
#             if value == i:
#                 return(map["destination_range_start"]+i-map["source_range_start"])
#     return value
def map_value(maps,value):
    for map in maps:
        if value >= map["source_range_start"] and value <= map["source_range_start"]+map["range_length"]:

            return(map["destination_range_start"]-map["source_range_start"]+value)
    return value
current_category=""
categories = []
almanac= {}
seeds = {}
for l in f:
    if len(l) <= 1:
        continue
    if "seeds" in l:
        name, seed = l.split(":")
        seedarray = seed.split()
        for i,s in enumerate(seedarray):
            print("adding seeds",s,"-",str(int(seedarray[i])+int(seedarray[i+1])))
            if i%2==1:
                continue
            for r in range(int(seedarray[i]),int(seedarray[i])+int(seedarray[i+1])):
                seeds[r] = {}
        
    elif "map" in l:
        name, map=l.split()
        current_category=name
        categories.append(name)
        almanac[current_category] = []
    else:
        destination_range_start,source_range_start,range_length = l.split()
        almanac[current_category].append({
            "destination_range_start": int(destination_range_start),
            "source_range_start": int(source_range_start),
            "range_length": int(range_length)
        })

for seed in seeds:
    print("Seed:", seed)
    seeds[seed]["soil"] = map_value(almanac["seed-to-soil"],seed)
    # print("fertilizer")
    seeds[seed]["fertilizer"] = map_value(almanac["soil-to-fertilizer"],seeds[seed]["soil"])
    # print("water")
    seeds[seed]["water"] = map_value(almanac["fertilizer-to-water"],seeds[seed]["fertilizer"])
    # print("light")
    seeds[seed]["light"] = map_value(almanac["water-to-light"],seeds[seed]["water"])
    # print("temp")
    seeds[seed]["temperature"] = map_value(almanac["light-to-temperature"],seeds[seed]["light"])
    # print("humi")
    seeds[seed]["humidity"] = map_value(almanac["temperature-to-humidity"],seeds[seed]["temperature"])
    # print("location")
    seeds[seed]["location"] = map_value(almanac["humidity-to-location"],seeds[seed]["humidity"])

lowest = 99999999999999
for seed in seeds:
    if seeds[seed]["location"] <= lowest:
        lowest=seeds[seed]["location"]
print(lowest)
