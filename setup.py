from setuptools import setup

long_description = "stub"

setup(
    name="craftbook_lift_sign_generator",
    version="0.0.1",
    description="Automates the writing of signs for CraftBook lifts; rewrite of another program.",
    license="LGPL-2.1-or-later",
    long_description=long_description,
    author="AnarchoBooleanism",
    packages=["craftbook_lift_sign_generator"],
    install_requires=["keyboard"]
)