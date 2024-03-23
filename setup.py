#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pipelinewise-target-redshift",
    version="1.7.0",
    description="Singer.io target for loading data to Amazon Redshift - PipelineWise compatible",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="TransferWise",
    url="https://github.com/transferwise/pipelinewise-target-redshift",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    py_modules=["target_redshift"],
    install_requires=[
        "pipelinewise-singer-python==1.3.0",
        "boto3==1.34.51",
        "psycopg2-binary==2.9.9",
        "inflection==0.5.1",
        "joblib==1.3.2",
    ],
    extras_require={"test": ["pylint==2.17.5", "pytest==7.4.2", "mock==5.1.0", "coverage==7.3.1"]},
    entry_points="""
          [console_scripts]
          target-redshift=target_redshift:main
      """,
    packages=["target_redshift"],
    package_data={},
    include_package_data=True,
)
