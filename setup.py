from setuptools import find_packages, setup
setup(
    name='routeutils',
    packages=find_packages(include=['routeutils']),
    version='0.1.0',
    description='A lib with geo route functions',
    author='Techlab Klabin',
    license='MIT',
    install_requires=['numpy==1.19.5', 'geopy==2.1.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)