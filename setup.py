from distutils.core import setup
import signalsdb


setup(
    name='signalsdb',
    version=signalsdb.__version__,
    url='https://github.com/eugene-eeo/signalsdb',
    author='Eeo Jun',
    author_email='packwolf58@gmail.com',
    license='MIT',
    packages=['signalsdb'],
    description='Query Unix signals',
    long_description=open('README.rst').read(),
    keywords=['signals', 'unix', 'db'],
)
