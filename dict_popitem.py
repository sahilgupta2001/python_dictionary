# popitem() : popitem() method removes the last inserted item(in versions before 3.7, a random item is removed instead)
car = {"brand":"aston martin",
       "model": "V8 Ventage",
       "year": 2005
       }
car.popitem()
print(car) # {'brand': 'aston martin', 'model': 'V8 Ventage'}
