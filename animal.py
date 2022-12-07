from abc import ABC, abstractmethod


class Animal(ABC):

   name = ''


   def __init__(self):
       pass


   def sleep(self, time):
        self.time = time
        print('sleeeeep hours : '+' '+str(self.time))


   def make_sound(self,sound):
       self.sound = sound
       print(self.sound)

   @abstractmethod
   def move (self):
       pass


