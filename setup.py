import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), "emoji_data_python.py")

setuptools.setup(
    name="emoji_data_python",
    version="DEV",
    url="https://github.com/alexmick/emoji-data-python/",

    author="Alexander Micklewright",

    description="Python emoji toolkit",
    long_description="Full documentation available on https://emoji-data-python.readthedocs.io/en/latest/",

    zip_safe=False,
    platforms="any",

    python_requires=">=3.6.0",
    install_requires=[""],
    packages=setuptools.find_packages(),
    include_package_data=True,

    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
