import os
from pathlib import Path
from typing import Any, Dict


def parse_value(value: str) -> Any:
    """Converts string values to appropriate Python types."""
    
    value = value.strip()
    if value.lower() in ("true", "false"):
        return value.lower() == "true"
    
    if value.isdigit():
        return int(value)
    
    try:
        return float(value)
    except ValueError:
        pass

    return value


def load_env(file_path: Path) -> Dict[str, Any]:
    """Loads environment variables from a given .env file."""
    
    if not file_path.exists():
        return {}

    variables = {}
    with file_path.open() as file:
        for line in file:
            line = line.strip()
            
            if not line or line.startswith("#"):
                continue  # Skip empty or comment lines
            
            if "=" not in line:
                raise ValueError(f"Malformed line in .env file: '{line}'")

            key, _, value = line.partition("=")
            variables[key.strip()] = parse_value(value)

    return variables


variables = load_env(Path.cwd() / ".env")


def __getattr__(name):
    if name in variables:
        return variables[name]
    elif name in os.environ:
        return os.environ[name]
    raise AttributeError(f"Environment variable '{name}' not found.")


def __dir__():
    return list(variables.keys())
