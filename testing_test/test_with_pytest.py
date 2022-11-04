from .with_pytest import add
import pytest


@pytest.fixture()
def db():
    return 5


# @pytest.mark.number
def test_add(db):
    assert add(9, 21) == 30
    assert add(7, db) == 12
    assert add('Hello', ' world') == 'Hello world'
    assert 8 in (9, 12, 34, 8)


# @pytest.mark.strings
def add_test_with_strings():
    assert add('Hello', 'world') == 'hello world'


@pytest.mark.skip(reason='not yet ready for test')
def add_test_with_strings():
    assert add('Hello', 'world') == 'hello world'
