from machineid import __version__, __author__
from setuptools import setup

with open("README.md", "r") as fh:
  readme = fh.read()

setup(
  name='py-machineid',
  version=__version__,
  description='Get the unique machine ID of any host (without admin privileges)',
  long_description_content_type='text/markdown',
  long_description=readme,
  url='https://github.com/keygen-sh/py-machineid',
  author=__author__,
  author_email='oss@keygen.sh',
  license='MIT',
  install_requires=['winregistry; sys_platform == "win32"'],
  packages=['machineid'],
  package_data={
    'machineid': ['py.typed'],
  },
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
)
