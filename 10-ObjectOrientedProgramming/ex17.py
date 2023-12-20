"""
17.	In the TV class, add support for volume adjustment in the range 0 to 10. The initial value of 
the volume level is 0. Add two methods to increase and decrease the TV volume level by one. Note 
that you cannot increase or decrease the volume beyond the specified range. Display the current 
volume level in the show_status() method. Then check the operation of the TV by adjusting and 
displaying its volume level.
"""
class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on and self.channel_no <= len(self.channels):
            print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no -1]}), volume {self.volume}")
        elif self.is_on and self.channel_no > len(self.channels):
            print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
        else:
            print("TV is off")
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self,channels_list):
        self.channels = channels_list
    def show_channels(self):
        print(f"Channel list: {" ".join(str(x) for x in self.channels)}")
    def inc_vol(self):
        if self.volume < 10:
            self.volume += 1
        else:
            pass
    def dec_vol(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            pass

ex = TV()
x = ["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery","EskaTV"]
ex.show_status()
ex.turn_on()
ex.show_status()
ex.inc_vol()
ex.show_status()
ex.dec_vol()
ex.show_status()
ex.dec_vol()
ex.show_status()
ex.turn_off()
ex.show_status()