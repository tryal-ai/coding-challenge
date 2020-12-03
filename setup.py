from setuptools import setup, find_packages

setup(name='tryal-coding-challenge',
      version=open('VERSION').read(),
      description='Tryal.AI Coding Challenge',
      author='Adam Green',
      author_email='adam@tryal.ai',
      url='https://tryal.ai/',
      packages=find_packages(),
      install_requires=[],
      include_package_data=True
)
