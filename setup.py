from setuptools import setup

setup(
    name="django-more-password-validators",
    version=__import__("more_password_validators").__version__,
    author="Tom Samstag",
    author_email="tsamstag@securityinnovation.com",
    description=("A Django reusable app that provides additional password "
                 "validators"),
    long_description=open("README.rst").read(),
    url="http://github.com/tecknicaltom/django-more-password-validators/",
    license="BSD",
    packages=[
        "more_password_validators",
    ],
    include_package_data=True,
    install_requires = [
        "Django >= 1.9",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Utilities",
        "Framework :: Django",
    ],
)
