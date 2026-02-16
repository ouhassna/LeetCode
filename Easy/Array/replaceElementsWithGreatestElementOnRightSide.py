class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Replaces each element in the array with the greatest element among the elements to its right.
        The last element is replaced with -1.

        Approach:
        - Traverse the array from left to right.
        - Keep track of the maximum value seen so far from the right side.
        - For each element, replace it with the current maximum, then update the maximum.

        Time Complexity: O(n)
        Space Complexity: O(1) (in-place modification)

        :param arr: List of integers
        :return: Modified list where each element is replaced by the greatest element to its right
        """
        maxR = -1
        for i in range(len(arr) - 1,-1 , - 1):
            newMax = max(maxR, arr[i])
            arr[i] = maxR
            maxR = newMax
        return arr
