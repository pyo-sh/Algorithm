from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        def compareDef(x, y):
            if int(x + y) > int(y + x):
                return -1
            else:
                return 1
        result = "".join(sorted([str(n) for n in nums], key = cmp_to_key(compareDef)))
        return "0" if result[0] == '0' else result 