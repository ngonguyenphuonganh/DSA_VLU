class DynamicMatrix2D:
    def __init__(self):
        self.matrix = []
        self.cols = 0

    def add_row(self, row):
        if not self.matrix:
            self.cols = len(row)
        self.matrix.append(row)

    def add_col(self, val=0):
        for row in self.matrix:
            row.append(val)
        self.cols += 1

    def set(self, r, c, val):
        self.matrix[r][c] = val

    def get(self, r, c):
        return self.matrix[r][c]