"""
14.	In the TV class, add the channels attribute containing a list of available TV channel names 
(array). Initially, the array should be empty (TV not programmed, no available channels). 
Add set_channels(channels_list) and show_channels() methods in the TV class, which allows you to 
set channels on the TV and display the list of available channels. Sample list of available channels:
Channel list:
1. TVP1
2. TVP2
3. Polsat
4. TVN
5. Filmbox
6. Discovery
"""
class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self,channels_list):
        self.channels = channels_list
    def show_channels(self):
        print(f"Channel list: {" ".join(str(x) for x in self.channels)}")

ex = TV()
x = ["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"]
ex.show_status()
ex.turn_on()
ex.show_status()
ex.show_channels()
ex.set_channels(x)
ex.show_channels()
ex.show_status()
ex.turn_off()
ex.show_status()