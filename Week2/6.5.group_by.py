def group_by(func, iterable):
    """
    Group the elements of an iterable by the value returned by the given function.
    :param func: The function to be used to group the elements
    :param iterable: The iterable that pass to func
    :return:
    """
    result = {}
    for item in iterable:
        key = func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

print(group_by(len, ["hi", "bye", "yo", "try"]))