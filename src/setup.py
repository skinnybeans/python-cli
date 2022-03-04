import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="midnyte-sample",
    version="0.0.1",
    author="Henrik Axelsson",
    author_email="henrik.axelsson@midnytecity.com.au",
    description="A small example package",
    long_description="nothing yet",
    # long_description_content_type="text/markdown",
    url="https://github.com/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.10",
    entry_points = {
        'console_scripts': [
            'midnyte_sample = midnyte.cli:start'
        ]
    }
)