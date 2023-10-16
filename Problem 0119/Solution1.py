class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prev_row = [1, 1]
        for i in range(2, rowIndex + 1):
            cur_row = [1] * (len(prev_row) + 1)
            n = len(cur_row)
            for j in range(1,n-1):
                cur_row[j] = prev_row[j - 1] + prev_row[j]
            prev_row = cur_row
        return cur_row
