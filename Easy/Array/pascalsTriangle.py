from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result =[[1]]
        i = 0
        j = 0
        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            result.append(row)
        return result
        

def main():
    # sol = Solution()
    # numRows = 5 
    # result = sol.generate(numRows)
    # print("pascal : ")
    z = zip([1, 2], [3, 4])
    print(list(z))
    # for row in result:
    #     print(row)
if __name__ == "__main__":
    main()


        