class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns indices of the two numbers in `nums` that add up to `target`.
        
        Approach:
        - Use a hashmap (dictionary) to store each number's value -> index.
        - Then iterate through nums again to check if (target - current number) exists.
        - Ensure we do not use the same element twice by checking indices.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        
        # Step 1: Build a hashmap to map each value to its index
        hashmap = {}
        for i, value in enumerate(nums):
            hashmap[value] = i

        # Step 2: Iterate through nums to find the complement
        for i, value in enumerate(nums):
            diff = target - value
            # Check if complement exists in hashmap AND is not the same index
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]  # Return the pair of indices

        # If no pair found, return empty list
        return []

    

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if num[i] + num[j] == target:
#                     return [i, j]
#         return []