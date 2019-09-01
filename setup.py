from setuptools import setup, find_packages

with open('requirements.txt', 'r') as file:
    requirements = file.readlines()

setup(name='boto_manager',
      version='0.1',
      description='Abstracts the creation of boto clients and allows "injecting" mocking into AWS calls',
      url='https://github.com/sjdillon/boto_manager',
      author='sjdillon',
      author_email='sjdillon',
      license='MIT',
      packages=find_packages(),
      install_requires=requirements,
      zip_safe=True)
