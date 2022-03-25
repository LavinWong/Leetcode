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
        #we want to use odds element as much as possible
        for i in odds:
            #we just use all the first odd element
            if res == 0:
                res += i
            else:
                #if i == 1, nothing we can use
                if i == 1:
                    break
                #we can use even number of the odds elements
                res += (i-1)
        res += sum(evens)
        return res
