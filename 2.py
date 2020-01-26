list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2=[]
i=1
while i < len(list) :
    if list[i] > list[(i - 1)]:
        list2.append(list[i-1])
        list2.append(list[i])
    i+=2
print (list2)