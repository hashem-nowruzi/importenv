import os
from types import NoneType

import env


def test_boolean_variable():
    assert isinstance(env.BOOLEAN_VARIABLE, bool)
    assert env.BOOLEAN_VARIABLE is False


def test_integer_variable():
    assert isinstance(env.INTEGER_VARIABLE, int)
    assert env.INTEGER_VARIABLE == 42


def test_float_variable():
    assert isinstance(env.FLOAT_VARIABLE, float)
    assert env.FLOAT_VARIABLE == 3.14


def test_string_variable():
    assert isinstance(env.STRING_VARIABLE, str)
    assert env.STRING_VARIABLE == "hello_world"


def test_key_does_not_exist():
    assert isinstance(env.KEY_DOES_NOT_EXIST, NoneType)
    assert env.KEY_DOES_NOT_EXIST is None


def test__dir__():
    assert dir(env) == ['BOOLEAN_VARIABLE', 'FLOAT_VARIABLE', 'INTEGER_VARIABLE', 'STRING_VARIABLE']


def test_system_environment_variable():
    os.environ["KEY"] = "Value"
    
    assert isinstance(env.KEY, str)
    assert env.KEY == "Value"
