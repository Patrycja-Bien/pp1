"""
19.	The medical thermometer measures the patient's temperature in the range from 34.0 to 42.0 
degrees Celsius, with an accuracy of 0.1 degrees. Write a program in which define a class that 
describes the states and behaviors of the thermometer. The thermometer should enable temperature 
measurement (do it by generating a random number from the 34.0 to 42.0 range) and display the measured
value. If the temperature is at least 37 degrees Celsius, the thermometer should additionally display
the 'Fever' message, e.g.
Temperature: 37.2C (fever)
When the temperature is at least 41.0, the thermometer should additionally display the message 
'CRITICAL TEMPERATURE!!'. 
"""
import random

class Thermo():
    def __init__(self):
        self.temp = 0.0
        self.on = False
    def measure(self):
        if self.on:
            # Generate a random temperature between 34.0 and 42.0 with an accuracy of 0.1
            self.temp = round(random.uniform(34.0, 42.0), 1)

    def display(self):
        print(f"Temperature: {self.temp}C", end=" ")

        if self.temp >= 37.0:
            print("(fever)", end=" ")

        if self.temp >= 41.0:
            print("CRITICAL TEMPERATURE!!", end=" ")

        print()
    
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
