import re



f = open('Input.txt','r')

games = []

limits = {
    "green" : 13,
    "blue" : 14,
    "red" : 12
}


for l in f:
    gamenumber=re.match("Game\ (\d*)",l)[1]
    l=l[l.find(":")+2:]
    print("Game",gamenumber)
    games.append(gamenumber)
    for round in l.split(";"):
        for cubes in round.split(","):
            print(cubes.lstrip())
            cubecount, cubecolor = cubes.lstrip().split(" ")
            cubecount = int(cubecount)
            cubecolor = cubecolor.rstrip()
            if cubecount > limits[cubecolor]:
                print("game",gamenumber,"impossible")
                if gamenumber in games:
                    games.remove(gamenumber)


sum = 0
print(games)
for gameid in games:
    sum +=int(gameid)
print(sum)

