f = open("Beispiel.txt", "r")

for l in f:
    if "seeds" in l:
        name, seeds = l.split(":")
        seeds = seeds.split()
        print(seeds)
    