from distutils.core import setup

setup(name='codetempl',
    version='0.2.0',
    description='Code file generator',
    author='Fabian Meyer',
    author_email='user8324@posteo.net',
    scripts=['codetempl'],
    requires=['argparse', 'getpass', 'subprocess', 'json'],
    license='GPLv3')
