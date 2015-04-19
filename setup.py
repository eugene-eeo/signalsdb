from distutils.core import setup


setup(
    name='signalsdb',
    version='0.1',
    url='https://github.com/eugene-eeo/signalsdb',
    author='Eeo Jun',
    author_email='packwolf58@gmail.com',
    license='MIT',
    packages=['signalsdb'],
    description='Query Unix signals',
    long_description=open('README.rst').read(),
    keywords=['signals', 'unix', 'db'],
)
