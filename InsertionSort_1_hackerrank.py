n = int(input())
arr = input()
arr1 = arr.split()

val=arr1[n-1]

for i in range(n-2, -2, -1):
    arr = arr.split()
    if i == -1:
        arr[i+1] = val
        break
    elif int(arr[i])>int(val):
        arr[i+1]= arr[i]
    else:
        arr[i+1]= val
        break
    arr=' '.join(arr)
    print(arr)
arr=' '.join(arr)
print(arr)
    