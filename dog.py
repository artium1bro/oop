from animal import Animal

class Dog(Animal):

    def __init__(self,km):
        super().__init__()
        self.km = km


    def run(self):
        print('dog run' + ' '+str( self.km))

    def dog_sound(self):
        super().make_sound('aw aww')


    def move(self):
        print('dog move')

