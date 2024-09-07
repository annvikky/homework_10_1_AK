from functools import wraps


def log(filename=None):
    """Декоратор для логирования начала выполнения функции и ее результата в консоль
    или в заданный файл (при передаче параметра filename"""

    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if filename is None:
                print(f"{func.__name__} start")
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} ok")
                    return result
                except Exception as e:
                    print(
                        f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                    )

            else:
                with open(filename, "w") as file:
                    file.write(f"{func.__name__} start\n")
                    try:
                        result = func(*args, **kwargs)
                        file.write(f"{func.__name__} ok")
                        return result
                    except Exception as e:
                        file.write(
                            f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                        )

        return wrapper

    return inner
