class ClassPropertyDescriptor:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, objtype=None):
        if objtype is None:
            objtype = type(obj)
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget.__get__(obj, objtype)()

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def getter(self, func):
        self.fget = func
        return self

    def setter(self, func):
        self.fset = func
        return self

def class_property(func):
    if not isinstance(func, (staticmethod, classmethod)):
        func = classmethod(func)
    return ClassPropertyDescriptor(func)
