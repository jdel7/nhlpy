import setuptools

with open("README.md", "r") as fh:
        long_description = fh.read()

setuptools.setup(
        name = 'nhlpy',
        packages = ['nhlpy'],
        version = '0.1',
        description = 'An easy to use NHL API wrapper',
        author = 'Alexander Delgado',
        author_email = 'jobehico@gmail.com',
        url = 'https://github.com/0xalexdelgado/nhlpy',
        download_url = 'https://github.com/0xalexdelgado/nhlpy/archive/0.1.tar.gz',
        keywords = ['hockey', 'API', 'NHL', 'wrapper', 'api', 'nhlpy', 'statistics'],
        classifiers =(
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
        ),
)

