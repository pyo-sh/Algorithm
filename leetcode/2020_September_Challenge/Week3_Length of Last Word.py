class Solution:
    def lengthOfLastWord(self, s):
        return len(s.rstrip().split(" ")[-1])