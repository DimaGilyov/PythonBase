from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self):
        self.products = {"printer": [], "scanner": [], "xerox": []}

    def add(self, product):
        key = self.__get_type_product(product)
        self.products[key].append(product.get_info())

    # Куда перемещается товар со склада история умалчивает
    def moveTo(self, product):
        key = self.__get_type_product(product)
        for i, el in enumerate(self.products[key]):
            if el["id"] == product.id:
                # На этой прекрасной ноте мы закончим с этим методом
                self.products[key].pop(i)

    @staticmethod
    def __get_type_product(product):
        key = ""
        if type(product) == Printer:
            key = "printer"
        elif type(product) == Scanner:
            key = "scanner"
        elif type(product) == Xerox:
            key = "xerox"
        else:
            raise ValueError("Product type not found")

        return key

    def __str__(self):
        text = ""
        for key in self.products.keys():
            text += "\n"
            text += f"----------{key}, count: {len(self.products[key])}-------\n"
            for val in self.products[key]:
                text += f"{val}" + "\n"
        return text


class OfficeEquipment(ABC):
    def __init__(self, id, name, color):
        OfficeEquipment._check_arguments(id, name, color)
        self.id = id
        self.name = name
        self.color = color

    @staticmethod
    def _check_arguments(id, name, color):
        if not str(id).isdigit():
            raise ValueError("id is not number")
        if str(name).isdigit():
            raise ValueError("Name cannot be a number")
        if str(color).isdigit():
            raise ValueError("Name cannot be a number")

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def run(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, id, name, color, printing_technology):
        super().__init__(id, name, color)
        self.printing_technology = printing_technology
        if str(printing_technology).isdigit():
            raise ValueError("Printing technology cannot be a number")

    def run(self):
        print("Printer running")

    def get_info(self):
        return dict(id=self.id, name=self.name, color=self.color, printing_technology=self.printing_technology)

    def __str__(self):
        return "{" f"'id': {self.id}, 'name': '{self.name}', 'color':'{self.color}', " \
               f"'printing_technology': '{self.printing_technology}'" "}"


class Scanner(OfficeEquipment):
    def __init__(self, id, name, color, scanner_type):
        super().__init__(id, name, color)
        self.scanner_type = scanner_type
        if str(scanner_type).isdigit():
            raise ValueError("Scanner type cannot be a number")

    def run(self):
        print("Scanner running")

    def get_info(self):
        return dict(id=self.id, name=self.name, color=self.color, scanner_type=self.scanner_type)

    def __str__(self):
        return "{"f"'id': {self.id}, 'name': '{self.name}', 'color':'{self.color}', " \
               f"'scanner_type': '{self.scanner_type}'""}"


class Xerox(OfficeEquipment):
    def __init__(self, id, name, color, is_color):
        super().__init__(id, name, color)
        self.is_color = is_color
        if not type(is_color) is bool:
            raise ValueError("Color attr most be a boolean")

    def run(self):
        print("Xerox running")

    def get_info(self):
        return dict(id=self.id, name=self.name, color=self.color, is_color=self.is_color)

    def __str__(self):
        return "{"f"'id': {self.id}, 'name': '{self.name}', 'color':'{self.color}', " \
               f"'is_color': '{self.is_color}'""}"


class IdGenerator:
    def __init__(self, start=0):
        self.__id = start

    @property
    def id(self):
        val = self.__id
        self.__id += 1
        return val


# -----------------------------------------------------------------------------------
generator = IdGenerator()
warehouse = Warehouse()

printer_1 = Printer(generator.id, "Phaser 3020", "Black", "Laser")
printer_2 = Printer(generator.id, "Xiaomi", "Black", "LED")
printer_3 = Printer(generator.id, "HP LaserJet", "White", "Laser")
warehouse.add(printer_1)
warehouse.add(printer_2)
warehouse.add(printer_3)

scanner_1 = Scanner(generator.id, "FUJITSU ScanSnap", "Black", "Drum")
scanner_2 = Scanner(generator.id, "Epson Perfection V600 Photo", "Black", "Tablet")
scanner_3 = Scanner(generator.id, "Canon imageFORMULA P-208II", "White", "Manual")
warehouse.add(scanner_1)
warehouse.add(scanner_2)
warehouse.add(scanner_3)

xerox_1 = Xerox(generator.id, "FXerox VersaLink C405DN", "Black", True)
xerox_2 = Xerox(generator.id, "Canon Pixma G3411", "Black", True)
xerox_3 = Xerox(generator.id, "EPSON L810", "White", False)
warehouse.add(xerox_1)
warehouse.add(xerox_2)
warehouse.add(xerox_3)

print(warehouse)
print(end="\n\n")
warehouse.moveTo(scanner_2)
print(warehouse)
