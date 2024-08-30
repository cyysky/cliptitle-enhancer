from setuptools import setup, find_packages

setup(
    name="cliptitle",
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyperclip",
        "requests",
        "beautifulsoup4",
        "plyer",
        "infi.systray"
    ],
    entry_points={
        "console_scripts": [
            "cliptitle=cliptitle.clip_title_enhancer:main",
        ],
    },
    package_data={
        "cliptitle": ["icon.ico"],
    },
    author="FMCV",
    author_email="chong@fmcv.my",
    description="A clipboard monitor that adds titles to copied URLs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cyysky/cliptitle",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)