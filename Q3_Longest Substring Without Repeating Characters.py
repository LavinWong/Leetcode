class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        windowStart, windowEnd, sum = 0,0,0
        dict = {}
        
        while windowEnd != len(s):
            if s[windowEnd] in dict:
                if windowStart <= dict[s[windowEnd]]:
                    windowStart = dict[s[windowEnd]] + 1
            dict[s[windowEnd]] = windowEnd
            sum = max((windowEnd -  windowStart) + 1, sum)
            windowEnd += 1
 
        return sum
