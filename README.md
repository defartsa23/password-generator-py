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
# Output : {'password': '003462', 'level': 0, 'strength': 'terrible', 'message': 'password is too short'}

# to generate letter password
password = generate().letter()
# Output : {'password': 'kapebq', 'level': 0, 'strength': 'terrible', 'message': 'password is too short'}

# to generate numberic and letter password
password = generate().numberLetter()
# Output : {'password': 'q9hlWS11', 'level': 3, 'strength': 'strong', 'message': 'password is perfect'}

# to generate random password
password = generate().random()
# Output : {'password': 'm6P)^yz9b"966D9G4uTd.!8Ni7xU1o19', 'level': 4, 'strength': 'very strong', 'message': 'password is very perfect'}

# to check the strength of your password
check = check("Password")
# Output : {'valid': False, 'level': 2, 'strength': 'medium', 'message': 'password is good enough, but not strong'}
```

## Dev Dependencies
* [Safe](https://github.com/defartsa23/safe) from [lepture](https://github.com/lepture)

## Contributing

Questions, comments, bug reports, and pull requests are all welcome.

## License

This software is licensed under the [MIT license](./LICENSE).