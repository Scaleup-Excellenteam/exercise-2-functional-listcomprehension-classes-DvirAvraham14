import time

def timer(f, *args, **kwargs):
    """
    timer decorator, which prints the time taken to run a function.
    :param f: function to be timed.
    :param args: arguments to be passed to f
    :param kwargs: keyword arguments to be passed to f
    :return: wrapper function
    """
    start_time = time.time()
    result = f(*args, **kwargs)
    end_time = time.time()
    print(f"Function {f.__name__} took {end_time - start_time} seconds to run.")
    return result

# test the timer decorator
timer(print, "Hello World")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")