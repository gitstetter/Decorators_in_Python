# Imports
from functools import wraps

# Define decorator function
def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        # 1. Any code to execute BEFORE calling the decorated function
        'Initial code block'

        # 2. Call decorated function if a CONDITION is met (optional)
        if 'CONDITON':
            return func(*args, **kwargs)

        # 3. Code to execute/return INSTEAD of calling the decorated function
        'Some other code block'
        return 'Something else to return'

    return wrapper

