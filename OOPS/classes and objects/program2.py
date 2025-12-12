class Person:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

a = Person("toyata", 2010)
print(a.model)
print(a.brand)
