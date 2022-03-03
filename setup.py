import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

about = {}
with io.open(
    os.path.join(here, "tutorfigures", "__about__.py"), "rt", encoding="utf-8"
) as f:
    exec(f.read(), about)


setup(
    name="tutor-figures",
    version=about["__version__"],
    url="https://docs.tutor.overhang.io/",
    project_urls={
        "Documentation": "https://docs.tutor.overhang.io/",
        "Code": "https://github.com/overhangio/tutor-figures",
        "Issue tracker": "https://github.com/overhangio/tutor-figures/issues",
        "Community": "https://discuss.overhang.io",
    },
    license="AGPLv3",
    author="Overhang.io",
    author_email="contact@overhang.io",
    description="A Tutor plugin for Figures, the Open edX reporting and data retrieval app",
    long_description=readme,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["tutor>=13.0.0,<14.0.0"],
    python_requires=">=3.6",
    entry_points={"tutor.plugin.v0": ["figures = tutorfigures.plugin"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
