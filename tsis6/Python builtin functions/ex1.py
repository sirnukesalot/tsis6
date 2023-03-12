def multiply(myList) :
    result = 1
    for i in range(0,len(myList)):
        result = result * myList[i]
    return result

list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiply(list1))
print(multiply(list2))