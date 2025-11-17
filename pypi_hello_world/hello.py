"""Hello world function implementation."""


def hello(name: str) -> str:
    """
    Return a greeting message for the given name.

    Args:
        name: The name to greet.

    Returns:
        A greeting string in the format "Hello {name}".

    Raises:
        TypeError: If name is None.
    """
    if name is None:
        raise TypeError("name cannot be None")
    return f"Hello {name}"

