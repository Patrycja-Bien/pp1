"""
15.	In the TV class, make changes to the show_status() method so that it displays not only 
the selected channel number but also its name. When the selected channel number exceeds the 
list of available channels, the channel name is not displayed.
TV is on, channel 4 (TVN)
Then, try using the TV. Set at least 7 channels (seven TV stations), change channel numbers and 
display TV status every time.

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
        if self.is_on and self.channel_no <= len(self.channels):
            print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no -1]})")
        elif self.is_on and self.channel_no > len(self.channels):
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
x = ["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery","EskaTV"]
ex.show_status()
ex.turn_on()
ex.set_channels(x)
ex.show_channels()
ex.show_status()
ex.set_channel(2)
ex.show_status()
ex.set_channel(3)
ex.show_status()
ex.set_channel(4)
ex.show_status()
ex.set_channel(5)
ex.show_status()
ex.set_channel(6)
ex.show_status()
ex.set_channel(7)
ex.show_status()
ex.set_channel(8)
ex.show_status()
ex.turn_off()
ex.show_status()