from setuptools import setup, find_packages

setup(
    name='sniffMyPackets',
    author='catalyst256',
    version='1.0',
    author_email='catalyst256@gmail.com',
    description='A collection of local transforms relating to packets',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari>=0.5'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
