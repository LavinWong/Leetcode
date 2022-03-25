class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==1):
            return 1
            
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1
            
        odds = []
        evens = []
        for i in dic:
            if dic[i] % 2:
                odds.append(dic[i])
            else:
                evens.append(dic[i])
                
        odds.sort(reverse = True)
        res = 0
        for i in odds:
            if res == 0:
                res += i
            else:
                if i == 1:
                    break
                res += (i-1)
        res += sum(evens)
        return res
