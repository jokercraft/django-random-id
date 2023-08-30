from setuptools import setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='django_random_id',
    version='0.0.1',
    author="Serdar Ilarslan",
    description='A model base class which provides custom designed random integer primary keys to you Django models.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    py_modules=["django_random_id"],
    package_dir={'': 'src'},
    extras_require={
        "dev": ["pytest"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="django orm primary-key",
)
