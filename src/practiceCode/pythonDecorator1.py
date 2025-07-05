class CustomDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self,  *args, **kwargs):

        if not isinstance(args[1], str):
            raise InterruptedError
        else:
            return self.func
        


    # def __call__(self, *args, **kwargs):
    #     # Check all positional arguments
    #     for arg in args:
    #         if not isinstance(arg, str):
    #             raise TypeError(f"Argument '{arg}' is not a string!")

    #     # Optionally, check keyword arguments too
    #     for key, value in kwargs.items():
    #         if not isinstance(value, str):
    #             raise TypeError(f"Argument '{key}={value}' is not a string!")

    #     return self.func(*args, **kwargs)


