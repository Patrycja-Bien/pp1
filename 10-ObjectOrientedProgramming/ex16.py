"""
16.	Create a class that describes cell phones with at least 3 phone states and 2 behaviors. 
Define a text representation of an object. Then, create 2 objects. 
Display their features and call their bahaviors.
"""
class Phone():
    def __init__(self,brand,year,battery):
        self.brand = brand
        self.year = year
        self.battery = battery
        self.is_on = True
    def charge(self):
        if self.battery < 20:
            print("Low battery")
        elif self.battery >=20 and self.battery <= 99:
            print("Battery ok")
        else:
            print("Battery full")
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def __str__(self) -> str:
        return "Brand: "+self.brand+"\n"+"Year: "+str(self.year)+"\n"+"Battery: "+str(self.battery)+"%"

phone = Phone("Apple",2018,100)
print(phone)
phone.charge()

phone2 = Phone("Samsung",2020,10)

print(phone2)
phone2.charge()