class Solution:
    def scoreOfString(self, s: str) -> int:  
        result = 0  
        
        # Loop through each pair of consecutive characters
        for i in range(len(s) - 1):
            # Compute absolute difference between ASCII codes and add to result
            result += abs(ord(s[i]) - ord(s[i + 1]))
        
        # Return the total score
        return result
