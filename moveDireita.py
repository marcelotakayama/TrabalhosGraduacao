n = 1
list_1 = [1, 2, 3, 4, 5, 6] 
list_1 = (list_1[len(list_1) - n:len(list_1)] + list_1[0:len(list_1) - n]) 
print(list_1) 