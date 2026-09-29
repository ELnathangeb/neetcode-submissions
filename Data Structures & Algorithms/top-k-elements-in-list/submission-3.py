'''
Understand

input: we get an array and adm am interger ;
output: we retuhr k most frequent elements with in the array so basically which eveyy numbers gets repated a lot
egede cases: what if k is zero or the array is empty
Match: Array

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        sorted_nums = sorted(map, key=map.get, reverse=True)
        return sorted_nums[:k]
