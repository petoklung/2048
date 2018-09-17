data = []
for i in range(4):
    data.append(input().split())
direction = int(input("Insert your direction: "))
print(data)

# go left - 0 / go top - 1 / go right - 2 / go down - 3
for x in range(len(data)):
    for y in range(len(data)-1):
        print("X: ", x, ", Y: ", y, ", Data: ", data[x][y])
        if(direction == 0):
            if(data[x][y+1] == data[x][y]):
                data[x][y] = int(data[x][y]) + int(data[x][y+1])
                data[x][y+1] = data[x][(len(data)-2)]
                data[x][len(data)-2] = data[x][len(data)-1]
                data[x][len(data)-1] = 0

            elif (int(data[x][y+1]) == 0):
                # print("the next value is 0")
                if(int(data[x][len(data)-2]) != 0):
                    data[x][y+1] = data[x][len(data)-2]
                    data[x][len(data)-2] = 0
                    data[x][y] = int(data[x][y]) + int(data[x][y+1])
                    data[x][y+1] = 0
                    # print("if one")
                    if(int(data[x][len(data)-1]) != 0):
                        data[x][y+1] = data[x][len(data)-1]
                        data[x][len(data)-1] = 0
                        # print("if two")
                elif(int(data[x][len(data)-2]) == 0 and int(data[x][len(data)-1]) != 0):
                    data[x][y+1] = data[x][len(data)-1]
                    data[x][len(data)-1] = 0
                    data[x][y] = int(data[x][y]) + int(data[x][y+1])
                    data[x][y+1] = 0
                    # print("else one")

        if(direction == 2):
            if(data[x][len(data)-y-1] == data[x][len(data)-y-2]):
                data[x][len(data)-y-1] = int(data[x][len(data)-y-1]) + int(data[x][len(data)-y-2])
                data[x][len(data)-y-1] = data[x][y+1]
                data[x][y+1] = data[x][y]
                data[x][y] = 0

                if(int(data[x][y+1]) != 0 and int(data[x][len(data)-2]) == 0):
                    print("data[x][y] still have number")
                    data[x][len(data)-2] = data[x][y+1]
                    data[x][y+1] = 0

            elif (int(data[x][len(data)-2]) == 0):
                # print("the next value is 0")
                if(int(data[x][y+1]) != 0):
                    data[x][len(data)-2] = data[x][y+1]
                    data[x][y+1] = 0
                    data[x][len(data)-1] = int(data[x][len(data)-1]
                                               ) + int(data[x][len(data)-2])
                    data[x][len(data)-2] = 0
                    # print("if one")
                    if(int(data[x][y]) != 0):
                        data[x][len(data)-2] = data[x][y]
                        data[x][y] = 0
                        # print("if two")
                elif(int(data[x][y+1]) == 0 and int(data[x][y]) != 0):
                    data[x][len(data)-2] = data[x][y]
                    data[x][y] = 0
                    data[x][len(data)-1] = int(data[x][len(data)-1]
                                               ) + int(data[x][len(data)-2])
                    data[x][len(data)-2] = 0
                    # print("else one")

print(data)
