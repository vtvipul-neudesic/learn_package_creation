import random
import string


def generate_random_id(length: int) -> str:
    """Generate a random id with the given length.

    Args:
        length (int): The length of the id.

    Returns:
        str: The generated id.
    """
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
