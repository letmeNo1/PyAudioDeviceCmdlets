import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setuptools.setup(
    name="pyaudiodevice",
    version="1.0.5",
    author="hank.huang",
    author_email="hank.huang550@gmail.com",
    description="python version developed based on AudioDeviceCmdlets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/letmeNo1/PyAudioDeviceCmdlets",
    packages=setuptools.find_packages(),
    package_data={
        'pyaudiodevice': ['*.pyi', 'lib/AudioDeviceCmdlets.dll']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
