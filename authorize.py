class UnauthorizedError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

def authorize(username, password):
    """Decorator that checks if the provided credentials match predefined values.

    Args:
        username (str): username
        password (str): password
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check if the provided credentials match predefined values
            if username == "admin" and password == "password123":
                # Execute the function
                return func(*args, **kwargs)
            else:
                # Raise an UnauthorizedError
                raise UnauthorizedError("Unauthorized access")
        return wrapper
    return decorator


