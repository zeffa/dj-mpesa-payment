from setuptools import setup, find_packages

# noinspection PyPackageRequirements

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dj-mpesa-payment',
    version='1.0.0',
    author='Elijah Onduso',
    description='Mpesa payment gateway',
    long_description=long_description,
    author_email='zeffah.elly@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Django',
        'django-phonenumber-field',
        'phonenumbers',
        'python-dateutil',
        'requests'
    ],
)
