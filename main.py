from person import Person
from animal import Animal
from dog import  Dog
from bird import Bird
from factory import Fact

if __name__ == '__main__':
    # a = Animal()
    # a.sleep(3)
    #
    # a1 = Dog(10)
    # a1.sleep(3)
    # a1.run()
    # a1.dog_sound()
    #
    # bird1 = Bird(20)
    # bird1.bird_sound()
    # bird1.move()
    # a1.move()
    #r = Fact(3)
    #r.getObject().drink()
    obj1 = SingletonClass()
    print(obj1)

    obj2 = SingletonClass()
    print(obj2)

    p = Person()
