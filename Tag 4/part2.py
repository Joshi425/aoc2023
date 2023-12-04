from pprint import pprint
f = open("Input.txt","r")

total_points = 0
cards = {}
stack = []
for l in f:
    print(l)
    card,numbers = l.split(":")
    card = int(card.split()[1])
    cards[card] = {}
    
    winning_numbers, numbers_i_have = numbers.split("|")
    cards[card]["winning_numbers"] = winning_numbers.strip().split()
    cards[card]["numbers_i_have"] = numbers_i_have.strip().split()
    cards[card]["wins"] = 0
    for n in cards[card]["numbers_i_have"]:
        if n.isnumeric():
            if n in cards[card]["winning_numbers"]:
                cards[card]["wins"] += 1

for c in cards:
    print("card",c,"clones",stack.count(cards[c]))
    for i in range(cards[c]["wins"]):
        #print("original",c,"won adding card",c+i+1,"to the stack")
        stack.append(cards[c+i+1])
    for i,j in enumerate(stack):
        if j == cards[c]:
            for w in range(j["wins"]):
                #print("clone",c,"won adding",c+w+1)
                stack.append(cards[c+w+1])

print(len(stack)+len(cards))
    
    

