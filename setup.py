from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tithi-wa",
    version="0.0.1",
    description=
    "tithi-wa - WhatsApp-bot: Automate WhatsApp with selenium in python.",
    py_modules=["session"],
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Maskgirl/tithi",
    author="SuLagna Mukherjee",
    author_email="tithimukherjee12@gmail.com",
    install_requires=[
        "",
    ],
    extras_require={
        "dev": [
            "",
            "",
            "",
        ],
    },
)
