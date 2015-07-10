try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Framework :: Django',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    name='django-pyodbc-azure',
    version='1.2.9',
    description='Django backend for Microsoft SQL Server and Azure SQL Database using pyodbc',
    long_description=open('README.rst').read(),
    author='Michiya Takahashi',
    author_email='michiya.takahashi@gmail.com',
    url='https://github.com/michiya/django-pyodbc-azure',
    license='BSD',
    packages=['sql_server', 'sql_server.pyodbc'],
    install_requires=[
        'Django>=1.7.9,<1.8',
        'pyodbc>=3.0',
    ],
    classifiers=CLASSIFIERS,
    keywords='azure django',
)
