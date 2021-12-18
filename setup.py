from setuptools import setup

setup(
    name='synapse-nextcloud-oauth',
    version='0.1.0',
    description=' Nextcloud OAuth mapping provider for Synapse',
    url='https://github.com/mashedkeyboard/synapse-nextcloud-oauth',
    author='Curtis Parfitt-Ford',
    author_email='curtis@mashedkeyboard.me',
    license='Apache 2.0',
    packages=['synapse-nextcloud-oauth'],
    install_requires=['matrix-synapse'],
    classifiers=[],
)
