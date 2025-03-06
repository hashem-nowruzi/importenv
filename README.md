# envu

This package provides a convenient way to load environment variables from the `.env` file and system environment variables, automatically parsing them into appropriate Python types (`bool`, `int`, `float`, or `str`). It also allows you to access the loaded variables as attributes.

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
None

>>> env.MY_VARIABLE or "default_value"  # Get the variable with a default fallback
"default_value"

```

### Example: How do I use it with Django?

For a typical Django project, the `.env` file is placed like this:

```bash
my_project/
├── .env                 # Your environment variables
├── manage.py            # Django project entry point
├── my_project/          # Main application folder
│   ├── __init__.py
│   ├── settings.py      # Django settings file where .env is loaded
│   ├── urls.py
│   └── wsgi.py
└── apps/
    ├── app1/
    └── app2/
```

An example of Django settings

```python
import env
from unipath import Path

BASE_DIR = Path(__file__).parent


SECRET_KEY = env.SECRET_KEY
DEBUG = env.DEBUG or False
ALLOWED_HOSTS = env.ALLOWED_HOSTS.split(",")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.DJANGO_DB_NAME,
        "USER": env.DJANGO_DB_USERNAME,
        "PASSWORD": env.DJANGO_DB_PASSWORD,
        "PORT": env.DJANGO_DB_PORT or 5432,
        "HOST": env.DJANGO_DB_HOST or "localhost",
    }
}


EMAIL_HOST_PASSWORD = env.EMAIL_HOST_PASSWORD
EMAIL_HOST_USER = env.EMAIL_HOST_USER
EMAIL_PORT = env.EMAIL_PORT or 25
EMAIL_HOST = env.EMAIL_HOST or "localhost"
EMAIL_USE_TLS = env.EMAIL_USE_TLS or False

# ...
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
