#!/usr/bin/env pyhton

# Get the highest product of 3 numbers in a given list3

def  highest_productOftriplet(array):
    if len(array)  < 3 :
        print("no triplet exists")
        return -1
        maxproduct = 0
        for i in range(0, len(array)):
            print(array[i])
            for j  in range(i + 1, len(array)):
                for k  in range(j + 1, len(array)):
                    #if(array[i] * array[j] * array[k]) > maxproduct:
                        maxproduct = (array[i] * array[j] *  array[k])
                        print(maxproduct)
                        break
                         

        return maxproduct



# Driver code

array = [0, 3, 2, 4, 5]
print(highest_productOftriplet(array))
