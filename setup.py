from setuptools import setup

with open("README.rst","r") as fh:
	long_description = fh.read()
	
setup(name='snipeit',
      version='1.2',
	  long_description=long_description,
      long_description_content_type="text/markdown",
      description=("Python library to access the SnipeIT API"),
      url='https://github.com/allen-nathanield/SnipeIT-PythonAPI',
      author='Nathan Allen',
      author_email='allen.nathanield@gmail.com',
      license='MIT',
      packages=['snipeit'],
      install_requires=['requests','simplejson'],
      zip_safe=False)
