class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []

        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())
        print(cleaned)
        return cleaned == cleaned[::-1]
solution =Solution()
solution.isPalindrome("Was it a car or a cat I saw?")
