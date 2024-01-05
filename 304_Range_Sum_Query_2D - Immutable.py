# First naive solution, not constant time retrieval
# ~1800 ms, 18%

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixMatrix = []
        
        for i, row in enumerate(matrix):
            total = 0
            self.prefixMatrix.append([])
            for n in row:
                total += n
                self.prefixMatrix[i].append(total)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row1, row2 + 1):
            prefixR = self.prefixMatrix[i][col2]
            prefixL = self.prefixMatrix[i][col1 - 1] if col1 > 0 else 0
            result += (prefixR - prefixL)
        
        return result


# After watching a video explaining a different approach, wrote this soln:
# ~1000 ms, 98%
    
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixMatrix = []
        
        for i, row in enumerate(matrix):
            total = 0
            self.prefixMatrix.append([])
            for j, n in enumerate(row):
                total += n
                self.prefixMatrix[i].append(total + (self.prefixMatrix[i - 1][j] if i > 0 else 0))


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefixMatrix[row2][col2]
        result -= self.prefixMatrix[row2][col1 - 1] if col1 > 0 else 0
        result -= self.prefixMatrix[row1 -1][col2] if row1 > 0 else 0
        if row1 > 0 and col1 > 0:
            result += self.prefixMatrix[row1 - 1][col1 - 1]
        return result


# Neetcode soln, also ~1000 ms, uses 0 for first row/col instead of ternary

class NumMatrix:
    def __init__(self, matrix):
        self.sum_ = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i, line in enumerate(matrix):
            previous = 0
            for j, num in enumerate(line):
                previous += num
                above = self.sum_[i][j + 1]
                self.sum_[i + 1][j + 1] = previous + above


    def sumRegion(self, row1, col1, row2, col2):
        sum_col2 = self.sum_[row2 + 1][col2 + 1] - self.sum_[row1][col2 + 1]
        sum_col1 = self.sum_[row2 + 1][col1] - self.sum_[row1][col1]
        return sum_col2 - sum_col1