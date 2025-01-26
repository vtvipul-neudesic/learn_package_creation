# RandomIDGenLib

RandomIDGenLib is a simple library for generating random IDs. It provides easy-to-use functions to create unique identifiers for various purposes, such as user IDs, session tokens, and more.

## Features

- Generate random IDs of specified length
- Support for alphanumeric characters
- Lightweight and easy to integrate

## Installation

To install RandomIDGenLib, use the following command:

```bash
pip install git+https://github.com/vtvipul-neudesic/learn_package_creation.git
```

## Usage

Here's a basic example of how to use RandomIDGenLib:

```python
from randomidgenlib import generate_id

# Generate a random ID of length 10
random_id = generate_id(10)
print(random_id)
```

## Custom Character Set

You can also specify a custom character set for generating IDs:

```python
from randomidgenlib import generate_id

# Generate a random ID of length 10 using only digits
random_id = generate_id(10)
print(random_id)
```
