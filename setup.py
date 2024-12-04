from setuptools import setup, find_packages

setup(
    name='communator-vigicrues',
    version='0.4.0',
    packages=find_packages(where='.'),
    package_dir={'': '.'},
    install_requires=[
        'dbus-python',
        'pyvigicrues',
    ],
    entry_points={
        'console_scripts': [
            'commutator-vigicrues=commutator_vigicrues.main:main',
        ],
    },
    author='Guillaume Scigala',
    author_email='guillaume@scigala.fr',
    description='Vigicrues dameon',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gscigala/commutator-vigicrues',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    test_suite='tests',
)
