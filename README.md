# envu

This package provides a convenient way to load environment variables from a `.env` file, automatically parsing them into appropriate Python types (`bool`, `int`, `float`, or `str`). It also allows you to access the loaded variables as attributes.

**Features:**

- Parses `.env` file values into their correct types.
- Supports boolean, integer, float, and string conversions.
- Skips empty lines and comments.
- Raises an error for malformed `.env` lines or missing variables.
- Provides a `__dir__` method for inspecting available keys.

## Installation

```sh
pip install envu
```

## Usage

```python
>>> import env  # not envu

>>> env.KEY  # Access environment variables as attributes
'Value'

>>> env.DEBUG  # Boolean Variable
False

>>> env.SECRET_KEY  # String Variable
'fake-secret-key'

>>> env.POSTGRESQL_PORT  # Integer Variable
5432

>>> env.SLEEP_TIME  # Float Variable
1.5

>>> env.ALLOWED_HOSTS.split(",")  # Convert to a list
["localhost", "127.0.0.1", "example.com"]

>>> env.UNDEFINED_VARIABLE  # Undefined Variable
Traceback (most recent call last):
 ...
AttributeError: Environment variable 'UNDEFINED_VARIABLE' not found.

>>> hasattr(env, "KEY")  # Check if an environment variable exists
True

>>> getattr(env, "MY_VARIABLE", "default_value")  # Get the variable with a default fallback
"default_value"

```

## Running Tests

To run the tests, make sure you have `pytest` installed. You can install it using `requirements.txt`:

```sh
pip install -r requirements.txt
```

Then run:

```sh
pytest
```

This command will discover and execute all test cases in the project.
For more advanced options, you can refer to the [pytest documentation](https://docs.pytest.org/en/stable/).
