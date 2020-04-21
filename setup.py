import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zipfs",
    version="1.0.5",
    python_requires='>=3',
    author="yoarch",
    author_email="yo.managements@gmail.com",
    description="CLI tool to directly zip several files/folders or an existing folder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoarch/zipf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    entry_points={
        "console_scripts": [
        	"zipf = zipf.zipf:main",
        	"zipper = zipf.zipf:main"
        ]
    }
)
