from distutils.core import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'YOURPACKAGENAME',         # How you named your package folder (MyLib)
    packages = ['YOURPACKAGENAME'],   # Chose the same as "name"
    version = '0.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
    long_description=long_description,            # Give a long description about your library
    long_description_content_type='text/markdown',
    author = 'YOUR NAME',                   # Type in your name
    author_email = 'your.email@domain.com',      # Type in your E-Mail
    url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',
    }, 
    keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ], 'Programming Language :: Python :: 3.6',
)