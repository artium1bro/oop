from animal import Animal

class Bird(Animal):

    def __init__(self,km):
        super().__init__()
        self.km = km

    def fly(self ,x):
        self.x =x
        print ('fly' , self.x)


    def bird_sound(self):
        super().make_sound('lalalalalalala')

    def move(self):
        print('bird move')