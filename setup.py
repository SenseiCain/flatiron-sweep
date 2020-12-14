from setuptools import setup
setup(
    name = 'flation_sweep',
    version = '0.1.0',
    packages = ['flatiron_sweep'],
    entry_points = {
        'console_scripts': [
            'flatiron_sweep = flatiron_sweep.__main__:main'
        ]
    })