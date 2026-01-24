class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # we use a set to store numbers we have already seen
        hashset = set()

        # Iterate through each number in the list
        for num in nums:
            # if the number is already in the set,
            # a duplicate exists
            if num in hashset:
                return True

            # Otherwise, add the number to the set
            hashset.add(num)

        # if no duplicates are found, we return  False
        return False


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#     for i in range(len(nums))
#         for j in range(i + 1, len(nums))
#             if nums[i] == nums[j]:
#                 return True
#     return False