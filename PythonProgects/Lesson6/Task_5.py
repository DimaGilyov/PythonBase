class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Drawing stationery {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Drawing pen {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Drawing pencil {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Drawing handle {self.title}")


# ----------------------------------------------------------
pen = Pen("Torpedo Blue-Rose")
pen.draw()

pencil = Pencil("Meisterstück Classique")
pencil.draw()

handle = Handle("COPIC")
handle.draw()
