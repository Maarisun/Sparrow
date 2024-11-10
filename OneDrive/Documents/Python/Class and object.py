
class laptop:
    def pricerange():
       print("15K-35K")
    def Processortype():
       print("i5,i7")
    def ramsize():
        print("8GB")

HP = laptop()
DELL = laptop()
Lenovo = laptop()

HP.price="25K"
DELL.price="35K"
Lenovo.price="40K"

HP.processor="i5"
DELL.processor="i3"
Lenovo.processor="i7"

HP.ram="8GB"
DELL.ram="8GB"
Lenovo.ram="8GB"

print("HP:",HP.price)
print(HP.processor)
print(HP.ram)

print("DELL:",DELL.price)
print(DELL.processor)
print(DELL.ram)

print("Lenovo:",Lenovo.price)
print(Lenovo.processor)
print(Lenovo.ram)

HP.pricerange()
