import os

from src.decorators import log


@log()
def my_function(x, y):
    return x / y


filename = "mylog.txt"


@log(filename=filename)
def my_function_2(x, y):
    return x / y


def test_log(capsys):
    # тест на корректность работы декоратора с выводом в панель
    my_function(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function start\nmy_function ok\n"


def test_log_with_raise(capsys):
    # тест на корректность работы декоратора с выводом в панель
    my_function(4, 0)
    captured = capsys.readouterr()
    assert captured.out.startswith("my_function start\nmy_function error")


def test_log_with_filename():
    # тест на корректность работы декоратора с выводом в отдельный файл
    my_function_2(4, 2)
    with open(filename, "r") as file:
        assert file.read() == "my_function_2 start\nmy_function_2 ok"
    os.remove(filename)


def test_log_with_filename_with_raise():
    # тест на корректность работы декоратора с выводом в отдельный файл
    my_function_2(4, 0)
    with open(filename, "r") as file:
        assert file.read().startswith("my_function_2 start\nmy_function_2 error")
    os.remove(filename)
