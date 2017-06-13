import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'emoji_data_python.py')

setuptools.setup(
    name="emoji_data_python",
    version="1.0.2",
    url="https://github.com/alexmick/emoji_data_python/",

    author="Alexander Micklewright",

    description="Python emoji toolkit",
    long_description="Full documentation available on http://pythonhosted.org/emoji-data-python",

    zip_safe=False,
    platforms='any',

    install_requires=[''],
    packages=setuptools.find_packages(),
    include_package_data=True,

    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
