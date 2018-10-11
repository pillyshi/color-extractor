from setuptools import setup, find_packages

setup(
    name = 'color-extractor',
    version = '0.0.1',
    url = 'https://github.com/pillyshi/color-extractor',
    author = 'pillyshi',
    author_email = 'pillyshi21@gmail.com',
    description = '',
    packages = find_packages(),
    install_requires = ['numpy', 'scikit-learn', 'opencv-python'],
)
