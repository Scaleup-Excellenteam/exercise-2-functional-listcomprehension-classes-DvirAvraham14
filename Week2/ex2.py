import functools

class InvalidTypeError(TypeError):
    pass

def type_checker(arg_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            if not isinstance(arg, arg_type):
                raise InvalidTypeError(f"Expected {arg_type.__name__} but got {type(arg).__name__}")
            return func(arg)
        return wrapper
    return decorator

@type_checker(int)
def square(x):
    return x ** 2

#print(square(5)) # Output: 25
#print(square('5')) # Raises InvalidTypeError: Expected int but got str