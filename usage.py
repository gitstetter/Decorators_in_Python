"""
Function decorators change the behavior of an existing function without the need to change the function’s actual code.
    * A decorator is a function
    * A decorator takes the decorated function as an argument
    * A decorator returns a new function
    * A decorator maintains the decorated function’s signature
"""

# Import decorator
from decorator_definition import decorator_name

# Define function and decorate
@decorator_name
def decorated_function('foo'):
    return 'bar'