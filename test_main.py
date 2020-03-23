import sys
sys.path.append('../python_lesson_4')
sys.path.append('../python_lesson_5')

import divisor_master as dv
import lib as l
import pytest

@pytest.fixture()
def divisors_10():
    return [1, 2, 5, 10]


@pytest.fixture()
def names():
    return ['Аня', 'Артур', 'Ильнур', 'Наиль', 'Алексей', 'Лена', 'Ксюша', 'Костя', 'Маша', 'Таня', 'Рая', 'Ясна', 'Север', 'Грег', 'Майя', 'Люба', 'Саша', 'Катя', 'Илья', 'Андрей']


def test_get_divisors(divisors_10):
    assert dv.get_divisors(10) == divisors_10


def test_is_simple():
    assert dv.is_simple(10) == False


def test_get_max_divisor():
    assert dv.get_max_divisor(10) == 10


def test_get_min_divisor_simple():
    assert dv.get_min_divisor_simple(10) == 2


def test_get_factors_simple():
    assert dv.get_factors_simple(10) == [2, 5]


def test_get_names_args(names):
    assert type(names) == list


def test_get_names_count(names):
    assert len(l.get_names(names, 100)) == 100


def test_get_names_contains(names):
    assert 'Артур' in l.get_names(names, 100)