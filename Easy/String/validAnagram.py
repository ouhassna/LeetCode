class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the strings have different lengths,
        # they cannot be anagrams
        if len(s) != len(t):
            return False

        # Sort both strings and compare them
        # If they contain the same characters
        # with the same frequencies, they are anagrams
        return sorted(s) == sorted(t)
