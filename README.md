# Password generator
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rand-pass-generator)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/rand-pass-generator)](https://pypi.org/project/sicboDice/)
[![PyPI - License](https://img.shields.io/pypi/l/rand-pass-generator)](https://opensource.org/licenses/MIT)

This module offers random password generation.

## Install

```bash
pip install rand-pass-generator
```

## Quick start

First of all, initialize:

```python
from rand_pass_generator import generate, check

# to generate numeric password
password = generate().number()

# to generate letter password
password = generate().letter()

# to generate numberic and letter password
password = generate().numberLetter()

# to generate random password
password = generate().random()

# to check the strength of your password
check = check("Password")
```

## Contributing

Questions, comments, bug reports, and pull requests are all welcome.

## License

This software is licensed under the [MIT license](./LICENSE).