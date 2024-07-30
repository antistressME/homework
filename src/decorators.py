from functools import wraps


def log(filename="print"):
    def wrapper(func):

        @wraps(func)
        def innit(*args, **kwargs):
            try:
                func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except:
                log_message = f"{func.__name__} error: {Exception.__class__.__name__}. Inputs: {args}, {kwargs}"
            if filename == "print":
                print(log_message)
            else:
                with open(filename, "w") as file:
                    file.write(log_message)
            return log_message

        return innit

    return wrapper


@log()
def my_function(x, y):
    return x + y


my_function(1, 2)
