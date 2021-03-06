from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='example_pkg',
      version='0.1',
      description='Example of customised Package.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='example package',
      url='https://github.com/Tarifscd/test_package.git',
      author='Tarif',
      author_email='tarif@example.com',
      license='MIT',
      packages=['example_pkg'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)
