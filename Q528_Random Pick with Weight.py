class Solution(object):
    def gcd_many(self, s):
        g = 0
        for i in range(len(s)):
            if i == 0:
                g = s[i]
            else:
                g = self.gcd_2(g,s[i])

        return g
    
    def gcd_2(self, a,b):		
        a,b = max(a,b),min(a,b)
        if a%b == 0:
            return b
        else:
            return self.gcd_2(b,a%b)

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.elementlist = []
        totalnum = sum(w)
        x = self.gcd_many(w)
        for i in range(0,len(w)):
            k = w[i]/x
            while k > 0:
                self.elementlist.append(i)
                k -= 1
        

    def pickIndex(self):
        """
        :rtype: int
        """
        return random.choice(self.elementlist)
    


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()





class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum_sequence = []
        total = 0
        for weight in w:
            total += weight
            self.sum_sequence.append(total)
        self.total_sum = total



    def pickIndex(self):
        """
        :rtype: int
        """
        random_index = random.randint(1, self.total_sum)
        left, right = 0, len(self.sum_sequence) - 1
        while left <= right:
            mid = (left + right) // 2 
            if self.sum_sequence[mid] < random_index:
                left = mid + 1
            else:
                right = mid - 1
        return left
        #   1       6       3    | weights
        #   1       7       10   | sum sequence
        # (0,1)   (1,7)   (7,10) | range of sum sequnce index
        
        # when the random index fits in that range of sum sequnce index
        # we then return the index of that weight that we find when the
        # condition (sum sequence value >= random_index) is satisfied 
        # and left contains the index of weight that satisfies the condition
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
