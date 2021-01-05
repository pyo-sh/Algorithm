class Solution:
    def validMountainArray(self, arr):
        length = len(arr)

        if length < 3 or arr[0] >= arr[1]:
            return False
        i = 0
        while i < length - 1 and arr[i] < arr[i + 1]:
            i += 1
        middle = i
        while i < length - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        if middle < i and i == length - 1:
            return True

        return False