from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            print(str(len(s)) + "#")
        print(res)
        return res

    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            # print(length)
            res.append(str[ j + 1: j + 1 + length])
            print(j + 1 + length)
            i = j + 1 + length



solution = Solution()
solution.decode("2#hi4#tasa")