import pytest 

import env


def test_boolean_variable():
    assert hasattr(env, "BOOLEAN_VARIABLE") is True
    assert isinstance(env.BOOLEAN_VARIABLE, bool)
    assert env.BOOLEAN_VARIABLE is False


def test_integer_variable():
    assert hasattr(env, "INTEGER_VARIABLE") is True
    assert isinstance(env.INTEGER_VARIABLE, int)
    assert env.INTEGER_VARIABLE == 42


def test_float_variable():
    assert hasattr(env, "FLOAT_VARIABLE") is True
    assert isinstance(env.FLOAT_VARIABLE, float)
    assert env.FLOAT_VARIABLE == 3.14


def test_string_variable():
    assert hasattr(env, "STRING_VARIABLE") is True
    assert isinstance(env.STRING_VARIABLE, str)
    assert env.STRING_VARIABLE == "hello_world"


def test_key_does_not_exist():
    assert hasattr(env, "KEY_DOES_NOT_EXIST") is False
    with pytest.raises(AttributeError, match="Environment variable 'KEY_DOES_NOT_EXIST' not found."):
        env.KEY_DOES_NOT_EXIST


def test__dir__():
    assert dir(env) == ['BOOLEAN_VARIABLE', 'FLOAT_VARIABLE', 'INTEGER_VARIABLE', 'STRING_VARIABLE']
