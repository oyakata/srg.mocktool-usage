# -*- coding:utf-8 -*-
from setuptools import setup, find_packages


version = "0.1"
requirements = ["mock", "mox", "minimock", "flake8"]


def main():
    setup(
        name="srg.mocktool-usage",
        version=version,
        description="Python2.x mock tool usage.",
        install_requires=requirements,
        packages=find_packages("src"),
        package_dir={"": "src"},
        author='Imagawa Yakata',
        author_email='imagawa.yakata@gmail.com',
        url='https://github.com/oyakata/mockusage',
        license='gpl',
    )


if __name__ == "__main__":
    main()
