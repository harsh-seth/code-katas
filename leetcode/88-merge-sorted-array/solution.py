def merge(arr1, m, arr2, n):
    i = m-1
    j = n-1
    for free_spot in range(m+n-1, -1, -1):
        if j == -1:
            arr1[free_spot] = arr1[i]
            i = i-1
        elif i == -1 or arr2[j] > arr1[i]:
            arr1[free_spot] = arr2[j]
            j = j-1
        else:
            arr1[free_spot] = arr1[i]
            i = i-1

arr1 = [1, 3, 5, 7, 0, 0, 0, 0]
arr2 = [2, 4, 6, 8]
merge(arr1, 4, arr2, len(arr2))
print(arr1)

arr1 = [2, 4, 6, 8, 0, 0, 0, 0]
arr2 = [1, 3, 5, 7]
merge(arr1, 4, arr2, len(arr2))
print(arr1)

arr1 = [1, 3, 5, 7]
arr2 = []
merge(arr1, 4, arr2, len(arr2))
print(arr1)

arr1 = [1, 3, 5, 7, 0, 0, 0, 0]
arr2 = [1, 3, 5, 6]
merge(arr1, 4, arr2, len(arr2))
print(arr1)
