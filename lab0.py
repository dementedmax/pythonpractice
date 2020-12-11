list_1 = [0,1,2,3,4,5,6,7,8,9]
list_2 = [0,2,3,4,7,8,12]

counter = 0

for i in list_1:
    if i in list_2:
        counter += 1

print(counter)