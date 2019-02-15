from setuptools import setup

setup(
    name="pyclick",
    version='0.1',
    packages=['pyclick'],
    install_requires=[
        'Click',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
    entry_points={
        'console_scripts': ['pyclick=pyclick.command_line:main']
    },
    include_package_data=True,
    zip_safe=False)