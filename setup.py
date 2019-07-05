from setuptools import setup
import etcampy

setup(
    name = 'etcampy',
    version = etcampy.__version__,
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
