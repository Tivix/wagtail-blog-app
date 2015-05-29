import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail_blog',
    version='0.1.0',
    packages=['wagtail_blog'],
    include_package_data=True,
    description='Simple wagtail blog.',
    long_description=README,
    install_requires=[
        'Django>=1.7.0',
        'wagtail>=0.8',
    ],
    url='http://www.tivix.com/',
    author='Sumit Chachra',
    author_email='chachra@tivix.com',
    classifiers =[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
