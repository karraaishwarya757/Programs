def sortb(array):
    n = len(array)

    for i in range(n-1):

        for j in range(0, n-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

array = [18,3,52,84,100]
 
sortb(array)

for i in range(len(array)):
    print ("% d" % array[i])
