from setuptools import setup, find_packages

setup(
    name='sphinx-timetravel',
    version='0.1.0',
    description='Sphinx plugin for displaying timelines with year/month resolution',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/sphinx-timetravel',
    packages=find_packages(),
    install_requires=[
        'Sphinx>=4.0',
    ],
    entry_points={
        'sphinx.extensions': [
            'sphinx_timetravel = sphinx_timetravel:setup',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx',
    ],
)
