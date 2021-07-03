def solution(numbers, hand):
    answer = []
    
    nowLeft = 10
    nowRight = 12
    
    for num in numbers:
        if num in [1, 4, 7]:
            nowLeft = num
            answer.append('L')
        elif num in [3, 6, 9]:
            nowRight = num
            answer.append('R')
        else:
            if num == 0:
                num = 11
            leftAb = abs(num - nowLeft)
            rightAb = abs(num - nowRight)
            
            if sum(divmod(leftAb, 3)) > sum(divmod(rightAb, 3)):
                answer.append('R')
                nowRight = num
            elif sum(divmod(leftAb, 3)) < sum(divmod(rightAb, 3)):
                answer.append('L')
                nowLeft = num
            else:
                if hand == 'left':
                    answer.append('L')
                    nowLeft = num
                else:
                    answer.append('R')
                    nowRight = num
                
    return ''.join(answer)