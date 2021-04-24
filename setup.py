from setuptools import setup, find_packages
filepath = 'README.md'
setup(
        name="micropython-lagan",
        version="1.4",
        description="log system",
        long_description=open(filepath, encoding='utf-8').read(),
        long_description_content_type="text/markdown",
        author="jdh99",
        author_email="jdh821@163.com",
        url="https://github.com/jdhxyy/lagan-micropython",
        packages=find_packages(),
        data_files=[filepath]
    )
