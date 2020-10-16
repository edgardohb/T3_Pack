import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="T3_Pack", # Replace with your own username
    version="0.0.1",
    author="edgardohb",
    author_email="edghb25.ehb@gmail.com",
    description="Package for showing images, playing sounds, and counting words from a txt file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edgardohb/T3_Pack.git",
    package_dir= {'T3_Pack':'modules'},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts =['bin/images', 'bin/sound', 'bin/text'],
    install_requires = [
        'playsound',
        'matplotlib',
        'opencv-python',
        'tabulate',
    ],
    python_requires='>=3',
)
