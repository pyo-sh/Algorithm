def binary_search(sortedList, value):
    length = len(sortedList)
    left, mid, right = 0, length // 2, length

    while left <= right:
        if value == sortedList[mid]:
            return mid
        elif value > sortedList[mid]:
            left = mid + 1
            mid = (left + right) // 2 
        else:
            right = mid - 1
            mid = (left + right) // 2

    return -1

N = int(input())
points = list(map(int, input().split()))
sortedP = sorted(list(set(points)))

for num in points:
    print(binary_search(sortedP, num))