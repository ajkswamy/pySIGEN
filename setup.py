from setuptools import setup, find_packages
setup(
        name="pySIGEN",
        packages=find_packages(exclude=["^\."]),
        exclude_package_data={'': ["Readme.txt"]},
        install_requires=["numpy>1.3",
                          "pillow>=4.2.1"],
        python_requires=">=3.6",
)