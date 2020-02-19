import pytest


class AppError(Exception):
    pass


def inc(x):
    return x + 1


def raise_app_error():
    raise AppError()


def test_inc():
    assert inc(3) == 3


def test_raise_app_error():
    with pytest.raises(AppError):
        raise_app_error()
