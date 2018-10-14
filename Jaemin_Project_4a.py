#constants
ARRAY_SIZE = 85

#random ints
randomList = []
file = open('randomInts.txt', 'r')
for line in file.readlines():
    for i in line.split():
        randomList.append(int(i))


def merge_sort(inList, left, right):
    if (left < right):
        mid = (left + (right - 1)) // 2
        merge_sort(inList, left, mid)
        merge_sort(inList, mid + 1, right)
        merge(inList, left, mid, right)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * int((n1))
    R = [0] * int((n2))

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

dividedList = []
for i in range (0,ARRAY_SIZE//85):
  dividedList.append(randomList[i*85:(i + 1)*85])
  merge_sort(dividedList[i],0,len(dividedList[i])-1)
  print(dividedList[i])
