class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list = nums
        self.index = 0
        self.FirstUnique = 0
        self.change = None

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if(self.change):
            return self.change
        state = False
        while(self.index < len(self.list) and self.FirstUnique < len(self.list)):
            if(self.list[self.FirstUnique] == self.list[self.index] and self.FirstUnique != self.index):
                self.FirstUnique += 1
                self.index = 0
            elif(self.index + 1 == len(self.list)):
                state = True
                break
            else:
                self.index += 1
        if state:
            self.change = self.list[self.FirstUnique]
            return self.list[self.FirstUnique]
        else:
            return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if self.change == value:
            self.change = None
        self.list.append(value)
        return self.list


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
########################################################################################
class FirstUnique:

    def __init__(self, nums):
        self.c = Counter(nums)
        self.nums = nums

    def showFirstUnique(self):
        while self.nums and not self.c[self.nums[0]] == 1:
            self.nums.pop(0)
        for n in self.nums:
            if self.c[n] == 1:
                return n
        return -1
        

    def add(self, value):
        self.c[value] += 1
        self.nums.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
