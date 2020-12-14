from setuptools import setup
setup(
    name = 'flation-sweep',
    version = '0.1.0',
    packages = ['flatiron-sweep'],
    entry_points = {
        'console_scripts': [
            'flatiron-sweep = flatiron-sweep.__main__:main'
        ]
    })