import inspect


class Person:
    pass
def introspection_info(obj):
    return {'type': type(obj).__name__, 'атрибуты': obj.__dir__(), 'h': dir(obj), "u": inspect.getmodule(obj)}


g = Person()


print(introspection_info(g))