from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'All in one AIGC API package for Python'

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name="pgptAI",
    version=VERSION,
    author="QPython",
    author_email="support@qpython.org",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests', 'typing_extensions'],
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
