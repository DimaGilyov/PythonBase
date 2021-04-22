from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name="", param=0, tissue_consumption=None):
        self.__name = str(name)
        self.param = param
        self.tissue_consumption = tissue_consumption

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.tissue_consumption}"

    @property
    def param(self):
        """
        Clothes param (size or height)
        :return size or height:
        """
        return self.__param

    @param.setter
    def param(self, param):
        if param < 0:
            self.__param = 0
        else:
            self.__param = param

    @abstractmethod
    def calculation_tissue_consumption(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Coat(Clothes):
    def calculation_tissue_consumption(self):
        if self.tissue_consumption is None:
            return self.param / 6.5 + 0.5
        return self.tissue_consumption

    def __add__(self, other):
        tissue_consumption = self.calculation_tissue_consumption() + other.calculation_tissue_consumption()
        return Coat(tissue_consumption=tissue_consumption)


class Suit(Clothes):
    def calculation_tissue_consumption(self):
        if self.tissue_consumption is None:
            return 2 * self.param + 0.3
        return self.tissue_consumption

    def __add__(self, other):
        tissue_consumption = self.calculation_tissue_consumption() + other.calculation_tissue_consumption()
        return Suit(tissue_consumption=tissue_consumption)


coat_1 = Coat("BURBERRY", 6)
print(f"Coat_1 tissue consumption {coat_1.calculation_tissue_consumption():.2f}")

suit_1 = Suit("Nike", 5)
print(f"Suit_1 tissue consumption {suit_1.calculation_tissue_consumption():.2f}")

suit_2 = Suit("Adidas", 1)
print(f"Suit_2 tissue consumption {suit_2.calculation_tissue_consumption():.2f}", end="\n\n")

print(f"Sum tissue consumption: coat_1 + coat_2 + coat_3 = {coat_1 + suit_1 + suit_2}")
