from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ouput =[defaultdict[list]]
        for str in strs:
            count = [0] * 26 
            for i in str:
                count[ord(i) - ord("a")] += 1
            ouput[tuble(count)].append(str)
        return ouput.values()