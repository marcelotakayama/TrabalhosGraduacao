'''
TESTE 1 (USANDO APPEND)

def rightRotate(lists, num): 
    output_list = [] 
      
    # Will add values from n to the new list 
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item]) 
          
    return output_list 
  
# Driver Code 
rotate_num = 1
list_1 = [1, 2, 3, 4, 5, 6] 
  
print(rightRotate(list_1, rotate_num)) 
'''


n=1
def move(n, list_1):
    n = 1
    print(list_1) 


list_1 = [1, 2, 3, 4, 5, 6] 
list_1 = (list_1[-n:] + list_1[:-n]) 
    
    
    

move(n, list_1)




