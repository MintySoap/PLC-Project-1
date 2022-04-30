class Counter:

    def __init__(self):
        self._value = 1

    def get_value(self):
        return self._value

    def set_value(self,n):
        self._value = n

    def __str__(self):
        return str(self._value)

def main():
    c = Counter()
    print(c)
    c.set_value(c.get_value()+1)
    print(c)

#main()