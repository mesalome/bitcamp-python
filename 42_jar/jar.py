class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self.size = self.size + n
        if self.size > self.capacity:
            raise ValueError
        return self.size

    def withdraw(self, n):
        self.size = self.size - n
        if self.size < 0:
            raise ValueError
        return self.size

    @property
    def capacity(self):
        return int(self._capacity)
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
                raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
        return self._size


def main():
    jar = Jar()
    print(jar)

if __name__ =="__main__":
    main()