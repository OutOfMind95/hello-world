class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return f"🍪 * {self.n}"

    @classmethod
    def deposit(self, n):
        n = int(input("Deposit: "))
        size = 0
        size += n
        return size

    def withdraw(self, n):
        n = int(input("Withdraw: "))


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity > 12:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self.size