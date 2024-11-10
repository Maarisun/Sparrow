class company():
    def __init__(self):
      self._companyname="youtube"

class b(company):
    pass

a=b()
print(a._companyname)
