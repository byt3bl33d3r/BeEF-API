from setuptools import setup, find_packages

setup(
    name='beefapi',
    version='0.2',
    description = 'Python library that facilitates interfacing with BeEF via it\'s RESTful API',
    url='https://github.com/byt3bl33d3r/BeEF-API',
    author='byt3bl33d3r',
    author_email='byt3bl33d3r@gmail.com',
    license='GNU',

    classifiers=[
        'Programming Language :: Python :: 2.7'
    ],

    keywords='beef BeEF API',
    packages=find_packages(),
    install_requires=['requests'],
    include_package_data=False,
)
