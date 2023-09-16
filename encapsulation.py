class Base:
    def __init__(self):
        self.a="Prabhat"
        self._b="Tiwari"
class Child(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling the private memeber of base class")
        print(self._b)

obj1=Base()
print(obj1._b)
       
    
        