from setuptools import setup

setup(
    name = 'etcampy',
    version = '0.0.1',
    install_requires=['opencv-python'],
    packages = [
        'etcampy',
    ],
    package_dir={'etcampy': 'etcampy'},
    entry_points={
        "console_scripts": [
            "etcampy = etcampy.main:main",
        ]
    }
)
