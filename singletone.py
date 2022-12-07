from singletone import SingletonClass

class SingletonClass():
    _instances = None

    def __new__(cls):
        if cls_instance is None:
            print('creating the object')
            cls.__instances = super(SingletonClass , cls).__new__(cls)
        return cls._instances
