### setup.py file 
# from setuptools import setup
# with open("requirements.txt", "r") as fh:
#     requirements = fh.readlines()
# setup(
#    name = 'docopt-demo',
#    author = 'JonathanL',
#    description = 'Example of the setup file for the docopt demo',
#    version = '0.1.0',
#    packages = ['docopt-demo'],
#    install_requires = [req for req in requirements if req[:2] != "# "],
#    include_package_data=True,
#    entry_points = {
#       'console_scripts': [
#          'docopt = docopt-demo.docopt:main'
#       ]
#    }
# )