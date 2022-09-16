from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="1.0",
    entry_points ={"console_scripts":["cleanf=clean_folder.clean:main"],},
    description="Sort files in folder")
