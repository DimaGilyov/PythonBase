class Matrix:
    def __init__(self, matrix):
        self.__check_argument(matrix)
        self.__matrix = list(matrix)
        self.__columns_count = max(len(el) for el in self.__matrix)
        self.__try_padding_zeros()

    @staticmethod
    def __check_argument(arg):
        if not type(arg) is list:
            raise ValueError("Argument must be list (matrix)")
        elif len(arg) == 0:
            raise ValueError("Matrix length must be > 0")

        for row in arg:
            if not type(row) is list:
                raise ValueError("Matrix element must be list")
            for el in row:
                if not str(el).isdigit():
                    raise ValueError("Row element must be number")

    def __try_padding_zeros(self):
        for i, row in enumerate(self.__matrix):
            row = list(row)
            row_length = len(row)
            if row_length < self.__columns_count:
                self.__matrix[i].append(0)

    @property
    def matrix(self):
        return self.__matrix

    def get_rows_count(self):
        return len(self.__matrix)

    def get_columns_count(self):
        return self.__columns_count

    def __str__(self):
        text = ""
        for row in self.__matrix:
            text += "\t".join(str(e) for e in row) + "\n"
        return text

    def __add__(self, other):
        if self.get_columns_count() != other.get_columns_count() or self.get_rows_count() != other.get_rows_count():
            raise ValueError("Unequal number of rows or columns of matrix A and matrix B")

        new_matrix = []
        for i in range(self.get_rows_count()):
            new_row = []
            for j in range(self.get_columns_count()):
                new_row.append(self.__matrix[i][j] + other.matrix[i][j])
            new_matrix.append(new_row)
        return Matrix(new_matrix)


matrix_a = Matrix([[1, 2], [3, 4], [5]])
matrix_b = Matrix([[7, 8], [9, 10], [11, 12]])
matrix_c = matrix_a + matrix_b
print(f"{matrix_a}  + \n{matrix_b}  = \n{matrix_c}")
