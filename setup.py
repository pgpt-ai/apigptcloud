from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'All in one AIGC API package for Python'
LONG_DESCRIPTION = 'All in one AIGC API package for Python'

setup(
    name="pgptAI",
    version=VERSION,
    author="QPython",
    author_email="support@qpython.org",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'typing_extensions'],
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
