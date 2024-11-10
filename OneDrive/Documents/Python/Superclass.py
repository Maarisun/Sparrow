class a():
    def __init__(self):
        print("1")
    def display(self):
        print("1 is top")

class b(a):
    def __init__(self):
        print("2")
        super().__init__()
    def display(self):
        print("2 is next to 1")

class c(b):
    def display(self):
        print("c is next to b")
        
Apple=b()


