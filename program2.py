def count(k, lst):
    
    final_list = []
   
    for x in lst:
        if len(x) > k:
            final_list.append(x)
    return final_list

  
k = 4

n=int(input("Enter number of words: "))
lst = []
for i in range(n):
    element = input(" ")
    lst.append(element)


print("The words with more than 4 characters are:",count(k, lst))
