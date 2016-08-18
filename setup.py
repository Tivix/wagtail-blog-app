import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-blog-app',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    keywords = "django wagtail blog app tivix",
    description='Simple blog app for your Django Wagtail project.',
    long_description=README,
    install_requires=[
        'Django>=1.7.0',
        'wagtail>=1.0',
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
