class Student:
    def __init__(self, name, house): # customize the class __init__ is an instance method
        self.name = name
        self.house = house

    def __str__(self): # object seen as string
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    # Getter
    @property
    def house(self):
        return self._house # can't be the same name /line 6

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


def main():
    student = Student.get()
    print(student)



if __name__ == "__main__":
    main()
    