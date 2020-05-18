def SortingBigIntegers(unsorted): 
    
  # Direct sorting using lamda operator 
  # and length comparison 
  unsorted.sort(key = lambda x: (len(x), x)) 
  print ("\n".join(unsorted)) 

# Driver code of above implementation 
n = int(input())

unsorted = []

for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

SortingBigIntegers(unsorted)