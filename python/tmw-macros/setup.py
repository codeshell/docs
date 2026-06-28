"""
To installed the code
Install on the system with `uv add -e setup.py`
"""

from setuptools import setup

setup(
    name='tmw-macros',
    version='0.1.0',
    description="Test macros library for macros plugin",
    packages=['on_env', 'on_page_markdown', 'on_post_page'],
    license='MIT',
    author='codeshell'
)