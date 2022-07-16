"""setup script"""
from setuptools import setup, find_packages

with open("README.md", encoding='utf8') as f:
    long_description = f.read()

setup(
    name="calculator",
    version='1.0',
    description='Simple Calculator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='iwatake2222',
    author_email='abc@abc.com',
    url='https://github.com/iwatake2222/python_project_in_github',
    license='Apache License 2.0',
    install_requires=[
        "numpy",
    ],
    tests_require=['pytest'],
    packages=find_packages(),
    platforms=["linux", "unix"],
    python_requires=">3.7",
    entry_points="""
      [console_scripts]
      calculator=calculator.__main__:main
    """,
)
