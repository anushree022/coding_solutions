def Running_Time_of_Algorithms(ar):
    shift = 0
    for i in range(1, len(ar)):
        temp = ar[i]
        j = i
        while j > 0 and temp < ar[j-1]:
            ar[j] = ar[j-1]
            j -= 1
            shift += 1
        ar[j] = temp
        
    print (shift)

m = input()
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)
