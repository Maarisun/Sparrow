
class grandpa():
    def money(self):
        print("grandpa's money")

class land():
    def important(self):
        print("Improtant land")

class son1(grandpa,land):
  pass
class son2():
  pass


Mani=son1()

Mani.money()
Mani.important()
