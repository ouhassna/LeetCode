from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map ={}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        #sort key by thier values in descending order
        sort_nums = sorted(hash_map, key=hash_map.get, reverse=True)
        print(sort_nums)
        return sort_nums[:k]
#test the function 
solution = Solution()
solution.topKFrequent([1, 1, 2, 2, 2, 3, 3,3,3], 2)
            