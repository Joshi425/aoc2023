f = open("Input.txt","r")

for l in f:
    if "Time" in l:
        times = l.split()
        times.remove("Time:")
    elif "Distance" in l:
        distance = l.split()
        distance.remove("Distance:")
times=[int("".join(times))]
distance=[int("".join(distance))]
print(times)
print(distance)
win_chance = {}


for k,t in enumerate(times):
    t = int(t)
    win_chance[k] = 0
    for hold_time in range(0,t):
        hold_time = int(hold_time)
        travel_time = t-hold_time
        speed=travel_time*hold_time
        if speed > int(distance[k]):
            win_chance[k] += 1

print(win_chance)
