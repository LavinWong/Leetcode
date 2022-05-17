class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        if items is None:
            return None
        element = []
        ans = {}
        for i in items:
            if i[0] not in element:
                element.append(i[0])
                l1 = [i[1]]
                ans[i[0]] = l1
            else:
                if(len(ans[i[0]])<5):
                    l1 = ans[i[0]]
                    l1.append(i[1])
                    ans[i[0]] = l1
                else:
                    l1 = ans[i[0]]
                    minnum = min(l1)
                    if i[1] > minnum:
                        l1.remove(minnum)
                        l1.append(i[1])
                    ans[i[0]] = l1
        res = []
        element.sort()
        for j in element:
            tarlist = ans[j]
            meannum = sum(tarlist)/5
            res.append([j,meannum])
        return res
            
