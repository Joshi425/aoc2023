f = open("Input.txt","r")
content = f.readlines()

def is_symbol(string):

    if string == "." or string.isdigit() or string == "\n":
        return False
    return True
numbers = {}
for number,line in enumerate(content):
    numbers[number] = {}

for current_x,line in enumerate(content):
    for current_y,char in enumerate(line):
        if is_symbol(char):
            print("got symbol",char,"at x",current_x,"y",current_y)
            for x_offset in [-1,0,1]:
                for y_offset in [-1,0,1]:
                        temp_x = x_offset
                        if content[current_x+x_offset][current_y+y_offset].isdigit():
                            temp_y = y_offset
                            #print("number", content[current_x+x_offset][current_y+temp_y],"at x",current_x+x_offset,"y",current_y+y_offset )
                            
                            current_number = content[current_x+x_offset][current_y+temp_y]
                            temp_y-=1
                            while content[current_x+x_offset][current_y+temp_y].isdigit():
                                current_number = content[current_x+x_offset][current_y+temp_y]+current_number
                                temp_y-=1
                            number_start_y = temp_y+current_y
                            temp_y = y_offset
                            temp_y+=1
                            while content[current_x+x_offset][current_y+temp_y].isdigit():
                                current_number = current_number+content[current_x+x_offset][current_y+temp_y]
                                temp_y+=1
                            if not number_start_y in numbers[current_x+x_offset]:
                              numbers[current_x+x_offset][number_start_y] = current_number
                              #print("found number",current_number,"at x",current_x+x_offset,"y",number_start_y)
sum = 0
for x in numbers:
    for y in numbers[x]:
        print("found number",numbers[x][y],"at x",x,"y",y)
        sum+=int(numbers[x][y])

print("Sum",sum)