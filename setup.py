import setuptools

setuptools.setup(
    name = 'AlComplex',
    version = '1.0.1',
    packages = setuptools.find_packages(),

    author = 'Jean Franco Gómez',
    author_email = 'JeanFGomezR@gmail.com',

    description= 'An extended Complex number library',
    long_description = ''' An Alternative Complex Numbers
    Library. Inspired in the Ruby standard library complex numbers. 

    - Plays well with Python own numeric types (including own Python complex numbers).
    - Includes mathematic functiones specifically created to be compatible with complex numbers.''',

    license='MIT',
    url='https://github.com/Jexan/AlComplex',
)
