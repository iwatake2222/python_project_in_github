from setuptools import setup, find_packages

setup(
    name="calculator",
    version='1.0',
    description='Simple Calculator',
    author='iwatake2222',
    author_email='abc@abc.com',
    url='https://github.com/iwatake2222/python_project_in_github',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      calculator=calculator.__main__:main
    """,
)
