class Cell:
    def __init__(self, cell):
        if type(cell) != int:
            raise ValueError("Argument must be integer")
        self.cell = cell

    def make_order(self, row):
        full_rows_count = self.cell // row
        cells_remainder = self.cell - (full_rows_count * row)
        return ("*" * row + "\n") * full_rows_count + "*" * cells_remainder + "\n"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def __str__(self):
        return f"{self.cell}"


cell_1 = Cell(12)
cell_2 = Cell(7)
print(f"sum: {cell_1 + cell_2}")
print(f"sub: {cell_1 - cell_2}")
print(f"mul: {cell_1 * cell_2}")
print(f"div: {cell_1 // cell_2}", end="\n\n")

print(cell_1.make_order(5), end="\n\n")
print(cell_2.make_order(4), end="\n\n")
