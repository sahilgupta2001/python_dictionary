#items() - return a new view of the dictionary's items(key, value).
car = {"brand": "ford",
       "model": "mustang",
       "year": 1964
       }
x= car.items()

car["year"] = 2005 # change year

car["brand"] = "aston martin" # change brand values

car["model"] = "V8 Ventage" # change model values

car["speed"] = 205  # add speed in the dictionary

# pop() : pop() method removes the item with the specified key name
d = car.pop("year")

print(x) #dict_items([('brand', 'aston martin'), ('model', 'V8 Ventage'), ('speed', 205)])

print(d) #2005  
