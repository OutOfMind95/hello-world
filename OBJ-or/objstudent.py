class Student:
    def __init__(self, name, house, patronus): # customize the class __init__ is an instance method
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Missing house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): # object seen as string
        return f"{self.name} from {self.house}, patronus: {self.patronus}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return ":|"
            case "Jack Russell terrier":
                return ":O"
            case _:
                return ":("

def main():
    student = get_student()
    print(student)
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) # object created by the class with atribute(arguments)

if __name__ == "__main__":
    main()