class Solution(object):
    def merge(self, intervals):
        res = []
        #We sort the input list. In case to avoid the input like [[1,3],[8,10],[2,6],[15,18]].
        intervals.sort()
        #Initalize the last minumum value and the last maximum value to the 2 values of the first pair.
        last_min = intervals[0][0]
        last_max = intervals[0][1]
        for interval in intervals[1:]:
            #we campare each pair minumum value is less the last maximum value or not.
            if interval[0] <= last_max:
                #If it is does, which mean those two pairs have overlapping, so we need to reset the last maximum value is the current pair maximum value or the old last maximum value.
                last_max = max(last_max, interval[1])
            else:
                #if it is not, which means those two pairs did not have overlapping. so we add the pre-one to the res list.
                res.append([last_min, last_max])
                #reset the last minumum value and the last maximum value to find the next overlapping.
                last_min = interval[0]
                last_max = interval[1]
        #Add the last pair to the res list
        res.append([last_min, last_max])
        return res
                
