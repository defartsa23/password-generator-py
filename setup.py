from setuptools import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'rand_pass_generator',         # How you named your package folder (MyLib)
  packages = ['rand_pass_generator'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This module offers random password generator',   # Give a short description about your library
  long_description=long_description,            # Give a long description about your library
  long_description_content_type='text/markdown',
  author = 'Deza Farras Tsany',                   # Type in your name
  author_email = 'deza.ftsany@gmail.com',      # Type in your E-Mail
  url = 'https://defartsa.dev/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/defartsa23/password-generator-py/archive/refs/heads/main.zip',    # I explain this later on
  project_urls={
    'Documentation': 'https://github.com/defartsa23/password-generator-py',
    'Source': 'https://github.com/defartsa23/password-generator-py',
    'Tracker': 'https://github.com/defartsa23/password-generator-py/issues',
  }, 
  keywords = ['PASSWORD', 'GENERATOR', 'RANDOM'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: MacOS',
    'Operating System :: Microsoft',
    'Operating System :: Unix'
  ],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  test_suite='test'
)