class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if (words is None or k == 0):
            return None
        dictionary = collections.Counter(words)
        heap = []
        for key, value in dictionary.items():
            heap.append((-value,key))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]
