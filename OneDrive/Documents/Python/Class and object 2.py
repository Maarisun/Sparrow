class mobile():
    def __init__(self,brand,price,RAM):
        self.brand=brand
        self.price=price
        self.RAM=RAM
    def display(self):
        print("Brand:",self.brand)
        print("price:",self.price)
        print("RAM:",self.RAM)

Redmi=mobile("MI",12000,"8GB")
Redmi.display()
