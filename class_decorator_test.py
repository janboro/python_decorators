def retry(count):
    def decorator(function):
        def wrapper(self, *args, **kwargs):
            for _ in range(count):
                try:
                    return function(self, *args, **kwargs)

                except:
                    self.reset()

        return wrapper

    return decorator


class SomeClass:
    def reset(self):
        print("resetting")

    @retry(count=3)
    def my_func(self):
        print("method")


SomeClass().my_func()
