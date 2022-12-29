import pydanticio

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

pydanticio.setup(
    name='PydanticIO',
    version='0.0.1',
    author='Andrea Broccoletti',
    author_email='andrea.broccoletti@brockdev.it',
    description='Input and output pydantic models from/to json file',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BrockDeveloper/PydanticIO',
    license='CC',
    packages=['pydanticio'],
    install_requires=['pydantic'],
)