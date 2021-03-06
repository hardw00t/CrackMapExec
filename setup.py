from setuptools import setup, find_packages

setup(name='crackmapexec',
    version='4.0.0dev',
    description='A swiss army knife for pentesting networks',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
    ],
    keywords='pentesting security windows smb active-directory networks',
    url='http://github.com/byt3bl33d3r/CrackMapExec',
    author='byt3bl33d3r',
    author_email='byt3bl33d3r@protonmail.com',
    license='BSD',
    packages=find_packages(include=[
        "cme", "cme.*"
    ]),
    install_requires=[
        'pycrypto>=2.6',
        'pyasn1>=0.1.8',
        'gevent>=1.2.0',
        'bs4',
        'netaddr',
        'pyOpenSSL',
        'termcolor',
        'requests>=2.3.0',
        'msgpack-python'
    ],
    entry_points = {
        'console_scripts': ['crackmapexec=cme.crackmapexec:main', 'cme=cme.crackmapexec:main', 'cmedb=cme.cmedb:main'],
    },
    include_package_data=True,
    zip_safe=False)
