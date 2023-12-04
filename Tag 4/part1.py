f = open("Input.txt","r")

total_points = 0
for l in f:
    numbers = l.split(":")[1]
    winning_numbers, numbers_i_have = numbers.split("|")
    winning_numbers = winning_numbers.strip().split(" ")
    numbers_i_have = numbers_i_have.strip().split(" ")
    multiplier = 0
    for n in numbers_i_have:
        if n.isnumeric():
            if n in winning_numbers:
                print(n, "is in winning numbers multiplier",multiplier)
                if multiplier == 0:
                    multiplier = 1
                else:
                    multiplier*=2
    
    print("adding",multiplier)
    total_points +=multiplier

print(total_points)