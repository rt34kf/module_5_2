class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors


h = House('ЖК Эльбрус', 10)
h1 = House('ЖК Акация', 20)
print(h)
print(h1)
print(len(h))
print(len(h1))


