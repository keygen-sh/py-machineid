from setuptools import setup

with open("README.md", "r") as fh:
  readme = fh.read()

setup(
  name='py-machineid',
  version='0.3.0',
  description='Get the unique machine ID of any host (without admin privileges)',
  long_description_content_type='text/markdown',
  long_description=readme,
  url='https://github.com/keygen-sh/py-machineid',
  author='Zeke Gabrielse',
  author_email='oss@keygen.sh',
  license='MIT',
  install_requires=['winregistry'],
  packages=['machineid'],
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
)
