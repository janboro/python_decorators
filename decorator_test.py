def decorator(function):
    def wrapper():
        print("decorator")
        function()

    return wrapper


@decorator
def my_func():
    print("function")


my_func()
