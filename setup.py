from distutils.core import setup

setup(name='codetempl',
    version='0.3.0',
    description='Code file generator',
    author='Fabian Meyer, Julian Bopp',
    author_email='user8324@posteo.net, julian.bopp@physik.hu-berlin.de',
    scripts=['codetempl'],
    requires=['argparse', 'getpass', 'subprocess', 'json'],
    license='GPLv3')
