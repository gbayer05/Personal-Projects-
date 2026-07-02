#Gentry Bayer 
# 7/1/2026
# This was another workshop project that iw orked on in the freee code camp. 
# This is great for inventories, this is a very basic and beginner user friendly project. 

class MusicalInstrument:  # A class called Musical Instrument. This is the start of creating the inventory. 
    def __init__(self, name, instrument_type):  #This is a method with 3 parameters 
        self.name = name  #this is assigning parameters to instance_attributes 
        self.instrument_type = instrument_type # this is assiging another paremeter to an instance_attrribute 

    def play(self): # this is a the play method with only the self parameter 
        print(f'The {self.name} is fun to play!') # A print statement that is an f string, and it prints the name of the instrument that is fun to play. 

    def get_fact(self): #same as above just the get_fact method 
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.' #same type of print statement that is above, just includes name and type. 

#This section is creating instances. 
instrument_1 = MusicalInstrument('Oboe', 'woodwind') 
instrument_2 = MusicalInstrument('Trumpet', 'brass')

#Both these sections are calling the instances and printing the get_fact method. 
instrument_1.play()
print(instrument_1.get_fact())

instrument_2.play() 
print(instrument_2.get_fact())
