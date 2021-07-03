def solution(numbers, target):
    def allCheck(index, allSum):
        if index == len(numbers):
            if allSum == target:
                return 1
            else:
                return 0
            
        return allCheck(index + 1, allSum + numbers[index]) + allCheck(index + 1, allSum - numbers[index])

    return allCheck(0, 0)