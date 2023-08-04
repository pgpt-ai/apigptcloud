from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'All in one AIGC API package for Python'
LONG_DESCRIPTION = 'All in one AIGC API package for Python'

setup(

    name="apigptcloud",
    version=VERSION,

    # TODO
    author="quseit",
    author_email="<youremail@email.com>",

    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
