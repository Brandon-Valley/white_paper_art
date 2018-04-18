

class person():
    def __init__(self, name):
        self.name = name
        
class man(person):
    def __init__(self, dick_size, name):
        person.__init__(self,name)
        self.dick_size = dick_size
        

manA = man(7, 'bob')
print(manA.name)