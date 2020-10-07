from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tithiwa",
    version="0.0.4",
    description="tithiwa - WhatsApp-bot: Automate WhatsApp with selenium in python.",
    py_modules=["session", "messages"],
    packages=find_packages(),
    package_dir={"tithiwa": "tithiwa"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    license="MIT License",
    entry_points={
        'console_scripts': [
            'tithiwa = tithiwa.__main__:main',
        ],
    },
    url="https://github.com/Maskgirl/tithiwa",
    author="SuLagna Mukherjee",
    author_email="tithimukherjee12@gmail.com",
    install_requires=[
        "selenium",
    ],
    extras_require={
        "dev": [
            "",
            "",
            "",
        ],
    },
)
