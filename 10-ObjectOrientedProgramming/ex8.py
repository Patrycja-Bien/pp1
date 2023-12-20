"""
8.	Identify at least 3 states and 3 behaviors for a telephone object. Then, for the 
listed states and behaviors, create a class with fields (attributes) and methods. 
Try to use verbs in method names as they describe activities. 
Finally, create a object, call its methods and display object’s properties.
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

phone = Phone("Apple",2018,100)

print(f"My phone is from {phone.brand}.")
print(f"It was created in {phone.year},")
print(f"It's battery is {phone.battery}.")

phone.charge()

if phone.on:
    print("The phone is on.")
else:
    print("The phone is off.")

phone.off()

if phone.is_on:
    print("The phone is on.")
else:
    print("The phone is off.")