from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MULTI-AI AGENT",
    version="0.1",
    author="Mekky",
    packages=find_packages(),
    install_requires = requirements,
)


# This file is a Python package configuration script, commonly named setup.py. Its primary purpose is to define how a Python project is packaged, installed, and distributed. When someone installs this project using tools like pip, this file tells Python what the project is called, what version it is, who authored it, which packages should be included, and which external libraries are required for it to run.

# The file begins by importing setup and find_packages from the setuptools library. setuptools is a standard Python tool used for packaging and distributing Python projects. The setup function is the core function that describes the project’s metadata and installation behavior, while find_packages automatically discovers all Python packages inside the project directory, removing the need to manually list them.

# Next, the file opens the requirements.txt file and reads its contents. The requirements.txt file typically contains a list of third-party libraries required by the project, one per line. By reading this file and storing the dependencies in the requirements variable, the project ensures that the same dependencies are used both during development and installation. This approach avoids duplication and keeps dependency management consistent.

# The setup() function call defines the package metadata and installation instructions. The name parameter specifies the name of the package as it will be recognized by Python package managers. The version parameter indicates the current version of the project, which is important for tracking updates and managing releases. The author field records the name of the project’s author, providing ownership and attribution information.

# The packages=find_packages() line tells setuptools to automatically include all directories that contain an __init__.py file, treating them as Python packages. This is especially useful for larger projects, as it ensures that all modules in the project are bundled correctly without manually specifying each one.

# Finally, the install_requires=requirements parameter lists all external dependencies required for the project to function. When a user installs the project, Python will automatically install these dependencies if they are not already present. In this project, this would include libraries such as FastAPI, LangChain, Streamlit, and others defined in requirements.txt.

# In summary, this file acts as the installation blueprint for the multi-AI agent project. It ensures that the project can be installed, shared, and deployed in a clean, reproducible manner, making it suitable for both development and production environments.


## to run this file do "pip install -e ."
## this command should be run every time you create an __init__.py file or add a new package