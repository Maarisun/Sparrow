class laptop():
    def __init__(self):
        self.price=0
        self.storage=""
        self.processor=""
    def display(self):
        print("price:",dell.price)
        print("storage:",dell.storage)
        print("Purpose:Suitable for business use")

dell=laptop()
dell.price=25000
dell.storage="500 GB"

dell.display()
