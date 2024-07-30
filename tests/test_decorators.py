import pytest
from src.decorators import log

@log()
def my_func(x, y):
    return x + y

def test_log(capsys):
    my_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_func ok\n'


def test_log_type_error(capsys):
    my_func(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "my_func error: type. Inputs: (1, '2'), {}\n"


def test_log_no_args(capsys):
    my_func()
    captured = capsys.readouterr()
    assert captured.out == "my_func error: type. Inputs: (), {}\n"

def test_log_too_args(capsys):
    my_func(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert captured.out == "my_func error: type. Inputs: (1, 2, 3, 4), {}\n"