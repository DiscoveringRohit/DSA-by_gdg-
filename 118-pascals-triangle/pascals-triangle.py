class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        for _ in range(1, numRows):
            prev = rows[-1]
            row = [1]

            for i in range(1, len(prev)):
                row.append(prev[i-1] + prev[i])

            row.append(1)
            rows.append(row)

        return rows
