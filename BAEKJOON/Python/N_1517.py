import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

count = 0

def merge(start, end):
    global numbers, count
    merged_array = [0] * (end - start + 1)
    i = 0

    # 합병 하기
    center = (start + end) // 2
    left = start
    right = center + 1
    while left <= center and right <= end:
        # 왼쪽 선택
        if numbers[left] <= numbers[right]:
            merged_array[i] = numbers[left]
            left += 1
        # 오른쪽 선택
        # 오른쪽이 선택될 때 왼쪽이 얼마나 남아있는지가 swap 되는 횟수이다.
        elif numbers[right] < numbers[left]:
            merged_array[i] = numbers[right]
            right += 1
            count += center - left + 1
        i += 1
    
    # 남은 것을 처리하기 위함
    if right <= end:
        left = right
        center = end
    while left <= center:
        merged_array[i] = numbers[left]
        left += 1
        i += 1
    
    # 합병된 array 를 numbers로 옮기기
    i = 0
    for x in range(start, end + 1):
        numbers[x] = merged_array[i]
        i += 1

# 분배해서 merge 함수를 불러오도록 함
def partition(start, end):
    if start < end:
        center = (start + end) // 2
        partition(start, center)
        partition(center + 1, end)
        merge(start, end)

partition(0, N-1)

print(count)